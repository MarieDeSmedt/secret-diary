from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime


# all the crud (create, read, update and delete) methos to ensure data persistance

# #####################CUSTOMER##################################################"""

def get_all_cust(db: Session, skip: int = 0, limit: int = 100):
    """
    ask db for the list of all customers
    :param db: session
    :param skip:
    :param limit: len max of the list
    :return: list of customers
    """
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_cust(db: Session, customer: dict):
    """
    ask db to create a new customer
    :param db:
    :param customer: a dict with values for new customer attributes
    :return: the new customer create in db
    """
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
    """
    get a customer in db, with his name
    :param db: session
    :param name: str, name of the customer
    :return: a customer
    """
    return db.query(models.Customer).filter(models.Customer.name == name).first()


def get_cust_by_id(db: Session, id: int):
    """
    get a customer in db, with his id
    :param db: session
    :param id: int, id of the searched customer
    :return: a customer
    """
    return db.query(models.Customer).filter(models.Customer.id_customer == id).first()


def delete_cust_by_id(db: Session, id: int):
    """
    delete from the db a customer, define by his id
    :param db: session
    :param id: int, id of the choosen customer to delete
    :return: str, message if succefull
    """
    cust_to_delete = db.query(models.Customer).filter(models.Customer.id_customer == id).first()
    db.delete(cust_to_delete)
    db.commit()
    return "Successfully deleted"


def update_cust_by_id(db: Session, id: int, updated_cust: dict):
    """
    update oinformation of a choosen customer in db
    :param db: session
    :param id: int, id of the choosen customer to update
    :param updated_cust: dict, new values for the customer to update
    :return: the updated customer
    """
    cust_to_update = db.query(models.Customer).filter(models.Customer.id_customer == id).first()
    cust_to_update.name = updated_cust['name']
    cust_to_update.firstname = updated_cust['firstname']
    cust_to_update.information = updated_cust['information']
    cust_to_update.modification_date = updated_cust['modification_date']
    db.commit()
    db.refresh(cust_to_update)
    return cust_to_update


# ###########################################TEXT##################################################""


def create_text(db: Session, new_text: dict):
    """
    create a new text in db
    :param db: session
    :param new_text: dict, information to create the new text
    :return: the new text saved in db
    """
    text = models.Text(
        content=new_text['content'],
        creation_date=new_text['creation_date'],
        feeling=new_text['feeling'],
        score=new_text['score'],
        id_customer=new_text['id_customer']
    )
    db.add(text)
    db.commit()
    return text


def get_text(db: Session, id_text: int):
    """
    get text from db by its id
    :param db: session
    :param id_text: int, id from the choosen text
    :return: the choosen text
    """
    return db.query(models.Text).filter(models.Text.id_text == id_text).first()


def get_all_text(db: Session, skip: int = 0, limit: int = 100):
    """
    get the list of all the text in db
    :param db: session
    :param skip:
    :param limit: len max of the list
    :return: a list of texts
    """
    return db.query(models.Text).offset(skip).limit(limit).all()


def get_all_text_id_cust(id: int, db: Session, skip: int = 0, limit: int = 100):
    """
    get the list of texts writen by one choosen customer
    :param id: int, id of the choosen customer
    :param db: session
    :param skip:
    :param limit: len max of the list
    :return: list of texts
    """
    return db.query(models.Text).filter(models.Text.id_customer == id).offset(skip).limit(limit).all()


def delete_text(db: Session, text_to_delete: models.Text):
    """
    delete in the db a choosen text
    :param db: session
    :param text_to_delete: Text, the text to delete
    :return: message for successfullness
    """
    db.delete(text_to_delete)
    db.commit()
    return "Successfully deleted"
