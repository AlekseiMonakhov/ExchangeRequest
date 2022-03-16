from fastapi import FastAPI
from .routes import router
# from views import user_router, assets_router

app = FastAPI()
app.include_router(router)


@router.get('/data')
def getData():
    return

@router.post('/request')
def postRequest():
    return

app.include_router(prefix='/data', router=router)
# app.include_router(user_router)
# app.include_router(assets_router)
