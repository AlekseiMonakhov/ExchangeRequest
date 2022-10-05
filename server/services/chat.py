from sqlalchemy.future import select
from database.connection import Session, getSession
from fastapi import Depends
from database.tables import Messages


class MessagesService:
    def __init__(self, session: Session = Depends(getSession)):
        self.session = session

    async def addMessage(self, messageData: Messages):
        message = Messages(**messageData.dict())
        self.session.add(message)
        await self.session.commit()

    async def getList(
            self,
            chat_id: int,
    ) -> Messages:
        result = await self.session.execute(select(Messages).where(Messages.deal_id == chat_id))
        return result.scalars().all()
