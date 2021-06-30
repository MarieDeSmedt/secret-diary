from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from src.start.to_start import SessionLocal, db_connection
from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException, status

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
    customer = crud.get_cust(db, id_customer=id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


#
# @api.get("/customer")
# def get_all_customer():
#     """
#     return the list of all customers
#     :return: a dict
#     """
#     try:
#         df = pd.read_sql('SELECT * FROM {}'.format("customer"), con=db_connection)
#         result = df.to_json(orient="index")
#         response = json.loads(result)
#         return response
#     except:
#         print('Error:Unable to fetch data.')
#
#
# @api.post("/customer/{customer}")
# def create_customer():
#     return 'create_customer in process'
#
#
# @api.put("/customer/{id}")
# def update_cust(id):
#     return 'update_cust in process'
#
# @api.delete("/customer/{id}")
# def delete_cust_by_id(id):
#     print('start request')
#     # try:
#     #     print('delete')
#     #     cursor = mysql_connection.cursor()
#     #     cursor.execute("DELETE FROM customer WHERE id_customer={}".format(id))  # Execute SQL Query to detete a record
#     #     cu.commit()  # Commit is used for your changes in the database
#     #     print('Record deleted successfully...')
#     # except:
#     #     # rollback used for if any error
#     #     mysql_connection.rollback()
#     #     print('rollback...')
#     # mysql_connection.close()  # Connection Close
#
# # ###################   TEXT    ######################################################################
#
# @api.get("/text/{customerId}/{period}")
# def get_text_by_customerId_period(customerId, period):
#     return "get_text_by_customerId_period in process"
#
# @api.post("/text/{customerId}")
# def create_text(customerId):
#     return "create_text in progress"
#
# # ###################   FEELING    ######################################################################
# @api.get("/feeling/{customerId}/{period}")
# def get_avg_feeling_customerId_period(customerId,period):
#     return "get_avg_feeling_period in progress"
#
# @api.get("/feeling/{period}")
# def get_avg_feeling_all_period(period):
#     return "get_avg_feeling_all_period in process"