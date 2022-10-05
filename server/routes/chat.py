from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models.chat import Messages
from models.data import ErrorOutput
from services.chat import MessagesService


chat_router = APIRouter(
    prefix='/chat'
)


@chat_router.get(
    "/get-messages/{chat_id}",
    response_model=List[Messages],
    responses={400: {'model': ErrorOutput}}
)
async def getMessages(chat_id: int, service: MessagesService = Depends()):
    try:
        return await service.getList(chat_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@chat_router.post('/add-messages', response_model=Messages, responses={400: {'model': ErrorOutput}})
async def addMessage(messageData: Messages, service: MessagesService = Depends()):
    try:
        return await service.addMessage(messageData)
    except Exception as error:
        raise HTTPException(400, detail=str(error))
