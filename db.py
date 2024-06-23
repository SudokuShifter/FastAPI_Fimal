import databases
import sqlalchemy as SA
from sqlalchemy import ForeignKey
from settings import settings


DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = SA.MetaData()

users = SA.Table(
    'users',
    metadata,
    SA.Column('id', SA.Integer, primary_key=True),
    SA.Column('username', SA.String(20)),
    SA.Column('email', SA.String(40)),
    SA.Column('password', SA.String(40))
)

products = SA.Table(
    'products',
    metadata,
    SA.Column('id', SA.Integer, primary_key=True),
    SA.Column('title', SA.String(40)),
    SA.Column('description', SA.String(120)),
    SA.Column('price', SA.Integer, nullable=False, default=10)
)

orders = SA.Table(
    'orders',
    metadata,
    SA.Column('id', SA.Integer, primary_key=True),
    SA.Column('user_id', ForeignKey('users.id')),
    SA.Column('product_id', ForeignKey('products.id')),
    SA.Column('date', SA.String(120), nullable=False),
    SA.Column('status', SA.String(50))
)


engine = SA.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)