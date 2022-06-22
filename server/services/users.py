from datetime import (
    datetime,
    timedelta,
)
import json
from uuid import UUID

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordBearer
from jose import (
    JWTError,
    jwt,
)
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import users as models
from database import tables
from database.connection import Session, getSession
from models.users import User
from settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/user/sign-in/')


async def get_current_user(token: str = Depends(oauth2_scheme)) -> models.User:
    return await AuthService.verify_token(token)


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class AuthService:
    @classmethod
    async def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    async def verify_token(cls, token: str) -> models.User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')
        print("user_data: ", user_data)

        try:
            user = User.parse_obj(user_data)
            print(user)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    async def create_token(cls, user: tables.User) -> models.Token:
        user_data = models.User.from_orm(user)
        now = datetime.utcnow()
        encode_user_data = json.dumps(user_data.__dict__, cls=UUIDEncoder)
        encode_user_data_id = json.dumps(user_data.id, cls=UUIDEncoder)
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expires_s),
            'sub': encode_user_data_id,
            'user': encode_user_data,
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        print(token)
        return models.Token(access_token=token)

    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def register_new_user(
            self,
            user_data: models.UserCreate,
    ) -> models.Token:
        print(user_data)
        print("register_new_user"),
        user = tables.User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=self.hash_password(user_data.password),
        )
        print(user)
        self.session.add(user)
        await self.session.commit()
        return await self.create_token(user)

    async def authenticate_user(
            self,
            username: str,
            password: str,
    ) -> models.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        result = await self.session.execute(select(tables.User).where(tables.User.username == username))
        user = result.scalars().first()

        if not user:
            raise exception

        if not await self.verify_password(password, user.hashed_password):
            raise exception

        return await self.create_token(user)
