from fastapi import APIRouter, HTTPException
from db import products, database
from models.product import ProductIn, Product
from typing import List


router = APIRouter()


@router.get('/products/', response_model=List[Product])
async def get_products():
    try:
        query = products.select()
        return await database.fetch_all(query)
    except HTTPException(404, detail='Products not found'):
        return 'Please try again later'


@router.get('/products/{product_id}', response_model=Product)
async def get_some_product(product_id: int):
    try:
        query = products.select().where(products.c.id == product_id)
        return await database.fetch_one(query)
    except HTTPException(404, detail='Product not found'):
        return 'Please try again later'


@router.post('/products/', response_model=dict)
async def create_new_product(product: ProductIn):
    query = products.insert().values(**product.dict())
    await database.execute(query)
    return {'add new product': product}


@router.put('/products/{product_id}', response_model=Product)
async def update_product(product_id: int, product: ProductIn):
    try:
        query = products.update().where(products.c.id == product_id).values(**product.dict())
        return await database.fetch_one(query)
    except HTTPException(404, detail='Product not found'):
        return 'Please try again later'


@router.delete('/products/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': f'product with id {product_id} was deleted'}

