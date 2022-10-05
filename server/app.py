from fastapi import FastAPI
from routes.data import data_router
from routes.chat import chat_router
from routes.requests import request_router
import uvicorn
from routes.users import user_router
from settings import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

host = settings.server_host

origins = [
    f"http://{host}",
    f"http://{host}:8080",
    f"http://{host}:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data_router)
app.include_router(request_router)
app.include_router(user_router)
app.include_router(chat_router)

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )

