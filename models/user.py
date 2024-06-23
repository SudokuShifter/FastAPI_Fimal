from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """
    Оригинальная модель класса User
    """
    id: int
    username: str = Field(..., title='Name', min_length=1, max_length=20)
    email: EmailStr = Field(..., title='Email', min_length=5, max_length=40)
    password: str = Field(..., title='Password', min_length=5, max_length=40)


class UserIn(BaseModel):
    """
    Для взаимодействия в post-запросе
    """
    username: str = Field(..., title='Name', min_length=1, max_length=20)
    email: EmailStr = Field(..., title='Email', min_length=5, max_length=40)
    password: str = Field(..., title='Password', min_length=5, max_length=40)


class UserUp(BaseModel):
    """
    Для вывода в get-запросе
    """
    id: int
    username: str = Field(..., title='Name', min_length=1, max_length=20)
    email: EmailStr = Field(..., title='Email', min_length=5, max_length=40)