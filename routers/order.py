from fastapi import APIRouter, HTTPException
from db import orders, users, products, database
from models.order import Order, OrderIn
from typing import List
from datetime import datetime

router = APIRouter()


@router.get('/orders/', response_model=List[Order])
async def ger_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.get('/orders/{order_id}', response_model=Order)
async def get_some_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.post('/orders/', response_model=dict)
async def create_new_order(order: OrderIn):
    try:
        user_exists = await database.fetch_one(users.select().where(users.c.id == order.user_id))
        if not user_exists:
            raise HTTPException(400, detail='User ID does not exist')

        product_exists = await database.fetch_one(products.select().where(products.c.id == order.product_id))
        if not product_exists:
            raise HTTPException(400, detail='Product ID does not exist')

        date_obj = datetime.strptime(order.date, '%d/%m/%Y %H:%M')
        query = orders.insert().values(**order.dict())
        await database.execute(query)
        return {'create new order': order}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**order.dict())
    await database.execute(query)
    return {**order.dict(), 'id': order_id}


@router.delete('/orders/{order_id}', response_model=dict)
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': f'order with id {order_id} was deleted'}

