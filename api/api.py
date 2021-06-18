import pandas as pd

from fastapi import FastAPI
from src.start.to_start import db_connection


api = FastAPI()


# ###################   CUSTOMER    ######################################################################

@api.get("/customer/{id}")
def get_cust_by_id(id):
    name = "name"
    firstname = "firstname"
    information = "information"
    return {'name': name, 'firstname': firstname, 'information': information }


@api.get("/customer")
def get_all_customer():
    all_guest = []
    df = pd.read_sql('SELECT * FROM {}'.format("customer"), con=db_connection)
    response = df.to_json()
    return response


@api.post("/customer/")
@api.put("/customer/{id}")
@api.delete("/customer/{id}")
def delete_cust_by_id(customer_df, id):
    """
    delete one customer by id
    :param customer_df: dataset from customer table
    :param id: id of customer to delete
    :return:nan
    """
    return customer_df.drop(id)

# ###################   TEXT    ######################################################################

# ###################   FEELING    ######################################################################
