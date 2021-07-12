from enum import Enum
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from passlib.context import CryptContext
from pydantic import BaseModel


# #######################################CUSTOMER##########################"
class CustomerBase(BaseModel):
    pass


class Customer(CustomerBase):
    id_customer: int
    name: str
    firstname: str
    information: Optional[str] = "None"
    creation_date: str
    modification_date: Optional[str] = None
    deleted_date: Optional[str] = None

    class Config:
        orm_mode = True


class CustomerCreate(CustomerBase):
    name: str
    firstname: str
    information: Optional[str] = "None"
    creation_date: str


# ################################TEXT########################################""


class TextBase(BaseModel):
    pass


class Text(TextBase):
    id_text: int
    creation_date: str
    modification_date: Optional[str] = None
    deleted_date: Optional[str] = None
    id_customer: int
    content: str
    feeling: str
    score: int


    class Config:
        orm_mode = True
