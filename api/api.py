

from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from src.start.to_start import SessionLocal, db_connection
from fastapi import Depends, FastAPI, HTTPException

models.Base.metadata.create_all(bind=db_connection)

api = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ###################   CUSTOMER    ######################################################################

@api.get("/customer/{id}")
def get_cust_by_id(id: int, db: Session = Depends(get_db)):
    customer = crud.get_cust_by_id(db, id=id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@api.get("/customer/name/{name}")
def get_cust_by_name(name: str, db: Session = Depends(get_db)):
    customer = crud.get_cust_by_name(db, name=name)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@api.get("/customer", response_model=List[schemas.Customer])
def get_all_customer(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_all_cust(db, skip=skip, limit=limit)
    if customers is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customers


@api.post("/customer/", response_model=schemas.Customer)
def create_customer(new_cust: dict, db: Session = Depends(get_db)):
    cust = crud.get_cust_by_name(db=db, name=new_cust['name'])
    if cust:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_cust(db=db, customer=new_cust)


@api.put("/customer/{id}")
def update_cust_by_id(id: int, updated_cust: dict, db: Session = Depends(get_db)):
    return  crud.update_cust_by_id(db=db, id=id, updated_cust=updated_cust)

@api.delete("/customer/{id}")
def delete_cust_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_cust_by_id(db=db, id=id)




# # ###################   TEXT    ######################################################################
@api.get("/text/all/{id_customer}", response_model=List[schemas.Text])
def get_all_text_id_cust(id_customer: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    texts = crud.get_all_text_id_cust(id_customer, db, skip=skip, limit=limit)
    if texts is None:
        raise HTTPException(status_code=404, detail="texts not found")
    return texts


@api.get("/text/all/", response_model=List[schemas.Text])
def get_all_text(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    texts = crud.get_all_text(db, skip=skip, limit=limit)
    if texts is None:
        raise HTTPException(status_code=404, detail="texts not found")
    return texts


@api.get("/text/{id_text}", response_model=schemas.Text)
def get_text(id_text: int, db: Session = Depends(get_db)):
    text = crud.get_text(db, id_text)
    if text is None:
        raise HTTPException(status_code=404, detail="text not found")
    return text

@api.post("/text/", response_model=schemas.Text)
def create_ext(new_text: dict, db: Session = Depends(get_db)):
    return crud.create_text(db=db, new_text=new_text)


@api.delete("/text/{id}")
def delete_text_by_id(id: int, db :Session = Depends(get_db)):
    text = crud.get_text(db=db, id_text=id)
    if text is None:
        raise HTTPException(status_code=404, detail="text not found")
    return crud.delete_text(db=db,text_to_delete=text)

