from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String,
                        Numeric, Boolean, DateTime, ForeignKey)
from sqlalchemy.orm import scoped_session, sessionmaker

from datetime import datetime

class DataAccessLayer:
    connection = None
    engine = None
    db_session = None
    conn_string = None

    metadata = MetaData()

    users = Table('users', metadata,
        Column('id', Integer(), primary_key=True),
        Column('customer_number', Integer(), autoincrement=True),
        Column('name', String(255), nullable=False),
        Column('email_address', String(255), nullable=False, unique=True),
        Column('shipping_address', String(255), nullable=False),
        Column('phone_number', String(20), nullable=False),
        Column('password', String(25), nullable=False),
        Column('created_on', DateTime(), default=datetime.now),
        Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now))

    products = Table('products', metadata,
        Column('id', Integer(), primary_key=True),
        Column('product_number', Integer(), autoincrement=True),
        Column('name', String(255), nullable=False),
        Column('description', String(255), nullable=False),
        Column('unit_price', Numeric(12, 2), nullable=False),
        Column('seller_id', Integer(), ForeignKey('sellers.id')),
        Column('created_on', DateTime(), default=datetime.now),
        Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now))

    sellers = Table('sellers', metadata,
        Column('id', Integer(), primary_key=True),
        Column('seller_number', Integer(), autoincrement=True),
        Column('name', String(255), nullable=False),
        Column('email_address', String(255), nullable=False, unique=True),
        Column('password', String(25), nullable=False),
        Column('created_on', DateTime(), default=datetime.now),
        Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now))

    orders = Table('orders', metadata,
        Column('id', Integer(), primary_key=True),
        Column('order_number', Integer(), autoincrement=True),
        Column('user_id', Integer(), ForeignKey('users.id')),
        Column('orderd_on', DateTime, default=datetime.now),
        Column('shipped', Boolean(), default=False))

    orderItems = Table('orderItems', metadata,
        Column('id', Integer(), primary_key=True),
        Column('order_id', Integer(), ForeignKey('orders.id')),
        Column('product_id', Integer(), ForeignKey('products.id')),
        Column('quantity', Integer(), nullable=False),
        Column('extended_cost', Numeric(12, 2)))

    def db_init(self, conn_string):
        self.engine = create_engine(conn_string or self.conn_string)
        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=self.engine))
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()
        
dal = DataAccessLayer()