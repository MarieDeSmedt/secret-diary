from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status


# #####################CUSTOMER##################################################"""

def get_cust(db: Session, id_customer: int):
    return db.query(models.Customer).filter(models.Customer.id_customer == id_customer).first()


async def get_cust_by_name(db: Session, name: str):
    return db.query(models.Customer).filter(models.Customer.name == name).first()


async def get_all_cust(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


async def create_cust(db: Session, customer: schemas.Customer):
    new_cust = models.Customer(
        name=customer.name,
        firstname=customer.firstname,
        creation_date=datetime.today().strftime('%Y-%m-%d')
    )
    db.add(new_cust)
    db.commit()
    db.refresh(new_cust)
    return new_cust


async def delete_cust(db: Session, cust_to_delete: models.Customer):
    db.delete(cust_to_delete)
    db.commit()
    return "Successfully deleted"


# def update_cust(db: Session, cust_to_update: models.Customer, new_name: str, new_firstname: str, modification_date: str, new_information: str):
#     cust_to_update.name = new_name
#     cust_to_update.firstname = new_firstname
#     cust_to_update.modification_date = modification_date
#     cust_to_update.information = new_information
#     db.commit()
#     db.refresh(cust_to_update)
#     return "Successfully updated!"


async def update_cust(db: Session, current_cust: schemas.Customer, cust_update: schemas.Customer):
    updated_cust = get_cust(db, current_cust.id)
    updated_cust.name = cust_update.name
    updated_cust.firstname = cust_update.firstname
    updated_cust.modification_date = cust_update.modification_date
    updated_cust.information = cust_update.information
    db.commit()
    db.refresh(updated_cust)
    return updated_cust


# ###########################################TEXT##################################################""


async def create_text(db: Session, new_text: schemas.Text):
    new_text = models.Text(
        content=new_text.content,
        first_feeling=new_text.first_feeling,
        first_pourcentage=new_text.first_pourcentage,
        creation_date=datetime.today().strftime('%Y-%m-%d')
    )
    db.add(new_text)
    db.commit()
    db.refresh(new_text)
    return new_text


async def get_text(db, id_text: int):
    return db.get(models.Text, id_text)


async def get_all_text(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Text).offset(skip).limit(limit).all()


async def delete_text(db: Session, text_to_delete: models.Text):
    db.delete(text_to_delete)
    db.commit()
    return "Successfully deleted"
