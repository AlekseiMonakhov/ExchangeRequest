from multiprocessing import freeze_support

import uvicorn
from settings import settings

uvicorn.run(
    'server.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)


if __name__ == '__main__':
    freeze_support()
    ...

