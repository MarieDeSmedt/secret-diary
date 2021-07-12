from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float, Enum, Text
from sqlalchemy.orm import relationship
from src.start.to_start import Base


class Customer(Base):
    __tablename__ = "customer"

    id_customer = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=False, index=True)
    firstname = Column(String(20), unique=False, index=True)
    information = Column(String(255), unique=False, index=True)
    creation_date = Column(String(25), unique=False, index=True)
    modification_date = Column(String(25), unique=False, index=True)
    deleted_date = Column(String(25), unique=False, index=True)

    cust_text = relationship("Text", back_populates="writer")


class Text(Base):
    __tablename__ = "text"

    id_text = Column(Integer, primary_key=True, index=True)
    content = Column(String(255), unique=False, index=True)
    creation_date = Column(String(25), unique=False, index=True)
    modification_date = Column(String(25), unique=False, index=True)
    deleted_date = Column(String(25), unique=False, index=True)
    feeling = Column(String(25), unique=False, index=True)
    score = Column(Integer, unique=False, index=True)

    id_customer = Column(Integer, ForeignKey('customer.id_customer'))

    writer = relationship("Customer", back_populates="cust_text")
