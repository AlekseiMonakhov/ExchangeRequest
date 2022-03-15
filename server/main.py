from fastapi import FastAPI, APIRouter

# from views import user_router, assets_router

app = FastAPI()
router = APIRouter()

@router.get('/data')
def getData():
    return

@router.post('/request')
def postRequest():
    return

app.include_router(prefix='/data', router=router)
# app.include_router(user_router)
# app.include_router(assets_router)
