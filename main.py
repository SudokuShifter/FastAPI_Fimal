from fastapi import FastAPI
import uvicorn
from db import database
from routers.user import router as router_user
from routers.order import router as router_order
from routers.product import router as router_product

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


routers = [router_order, router_product, router_user]
for router in routers:
    app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )
