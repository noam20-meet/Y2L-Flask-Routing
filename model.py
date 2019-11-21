from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Product(Base):
   __tablename__ = 'Product'
   id = Column(String, primary_key=True)
   price = Column(Float)
   picturelink = Column(String)
   description = Column(String)


class Cart (Base):
   __tablename__ = 'Cart'
   product_id= Column(Integer, primary_key=True)
   



