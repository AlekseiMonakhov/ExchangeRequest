from fastapi import FastAPI
from routes.data import data_router
from routes.requests import request_router
import uvicorn
from settings import settings


app = FastAPI()
app.include_router(data_router)
app.include_router(request_router)

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )

