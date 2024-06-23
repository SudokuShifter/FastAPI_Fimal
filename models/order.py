from pydantic import BaseModel, Field, validator
from datetime import datetime, date


class Order(BaseModel):
    id: int
    user_id: int = Field(..., title='User_ID')
    product_id: int = Field(..., title='Product_ID')
    date: str
    status: str = Field(..., title='Status')


class OrderIn(BaseModel):
    user_id: int = Field(..., title='User_ID')
    product_id: int = Field(..., title='Product_ID')
    date: str = Field(default=str(datetime.now().strftime('%d/%m/%Y %H:%M')), title='Date: 12/12/2022 12:00')
    status: str = Field(..., title='Status')

    @validator('date')
    def validate_date(cls, v):
        try:
            datetime.strptime(v, '%d/%m/%Y %H:%M')
        except ValueError:
            raise ValueError('Incorrect date format, should be DD/MM/YYYY HH:MM')
        return v