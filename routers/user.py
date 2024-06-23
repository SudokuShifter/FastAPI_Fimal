from fastapi import APIRouter, HTTPException
from db import users, database
from models.user import UserIn, UserUp
from typing import List

router = APIRouter()


@router.get('/users/', response_model=List[UserUp])
async def get_users():
    try:
        query = users.select()
        return await database.fetch_all(query)
    except HTTPException(404, 'Users not found'):
        return 'Please try again later'


@router.get('/users/{user_id}', response_model=UserUp)
async def get_some_user(user_id: int):
    try:
        query = users.select().where(users.c.id == user_id)
        return await database.fetch_one(query)
    except HTTPException(404, 'User not found'):
        return 'Please try again later'


@router.post('/users/', response_model=dict)
async def create_user(user: UserIn):
    query = users.insert().values(**user.dict())
    await database.execute(query)
    return {'add new user': user}


@router.put('/users/{user_id}', response_model=dict)
async def update_data_user(user_id: int, user: UserIn):
    try:
        query = users.update().where(users.c.id == user_id).values(**user.dict())
        await database.execute(query)
        return {**user.dict(), 'id': user_id}
    except HTTPException(404, 'User not found'):
        return 'Please try again later'


@router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'User with id {user_id} was deleted'}
