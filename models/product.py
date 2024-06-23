from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    title: str = Field(..., title='Name_Product', min_length=10, max_length=40)
    description: str = Field(default=None, title='Description', min_length=10, max_length=120)
    price: int = Field(default=10, title='Price', ge=1, le=10000)


class ProductIn(BaseModel):
    title: str = Field(..., title='Name_Product', min_length=10, max_length=40)
    description: str = Field(default=None, title='Description', min_length=10, max_length=120)
    price: int = Field(default=10, title='Price', ge=1, le=10000)
