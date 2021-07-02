from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime


# #####################CUSTOMER##################################################"""

def get_all_cust(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_cust(db: Session, customer):
    new_cust = models.Customer(
        name=customer['name'],
        firstname=customer['firstname'],
        information=customer['information'],
        creation_date=datetime.today().strftime('%Y-%m-%d')
    )
    db.add(new_cust)
    db.commit()
    db.refresh(new_cust)
    return new_cust


def get_cust_by_name(db: Session, name: str):
    return db.query(models.Customer).filter(models.Customer.name == name).first()


def get_cust_by_id(db: Session, id: int):
    return db.query(models.Customer).filter(models.Customer.id_customer == id).first()


def delete_cust_by_id(db: Session, id: int):
    cust_to_delete = db.query(models.Customer).filter(models.Customer.id_customer == id).first()
    db.delete(cust_to_delete)
    db.commit()
    return "Successfully deleted"


def update_cust_by_id(db: Session, id: int, updated_cust: dict):
    cust_to_update = db.query(models.Customer).filter(models.Customer.id_customer == id).first()
    cust_to_update.name = updated_cust['name']
    cust_to_update.firstname = updated_cust['firstname']
    cust_to_update.information = updated_cust['information']
    cust_to_update.modification_date = updated_cust['modification_date']
    db.commit()
    db.refresh(cust_to_update)
    return "Successfully updated!"


# ###########################################TEXT##################################################""


def create_text(db: Session, new_text: dict):
    text = models.Text(
        content=new_text['content'],
        creation_date=new_text['creation_date'],
        first_feeling=new_text['first_feeling '],
        first_pourcentage=new_text['first_pourcentage'],
        second_feeling=new_text['second_feeling'],
        second_pourcentage=new_text['second_pourcentage'],
        third_feeling=new_text['third_feeling'],
        third_pourcentage=new_text['third_pourcentage'],
        id_customer=new_text['id_customer']
    )
    db.add(text)
    db.commit()
    return text


def get_text(db: Session, id_text: int):
    return db.query(models.Text).filter(models.Text.id_text == id_text).first()

def get_all_text(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Text).offset(skip).limit(limit).all()

def get_all_text_id_cust(id: int,db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Text).filter(models.Text.id_customer == id).offset(skip).limit(limit).all()


def delete_text(db: Session, text_to_delete: models.Text):
    db.delete(text_to_delete)
    db.commit()
    return "Successfully deleted"
