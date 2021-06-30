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
    first_feeling: str
    first_pourcentage: int
    second_feeling: Optional[str] = None
    second_pourcentage: Optional[int] = None
    third_feeling: Optional[str] = None
    third_pourcentage: Optional[int] = None

    class Config:
        orm_mode = True
