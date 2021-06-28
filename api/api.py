import pandas as pd
import json
from datetime import datetime
from typing import List
from fastapi import FastAPI
from src.start.to_start import db_connection, mysql_connection
from models.customer import Customer
from src.utils.mysql_utils import connect_to_mysql

api = FastAPI()


# ###################   CUSTOMER    ######################################################################

@api.get("/customer/{id}")
def get_cust_by_id(id):
    """
    return a customer choosed by id
    :param id: id  (int) of the choosen customer
    :return: a dict (one customer)
    """
    try:
        df = pd.read_sql('SELECT * FROM customer WHERE id_customer = {}'.format(id), con=db_connection)
        result = df.to_json(orient="index")
        response = json.loads(result)
        return response
    except:
        print('Error:Unable to fetch data.')


@api.get("/customer")
def get_all_customer():
    """
    return the list of all customers
    :return: a dict
    """
    try:
        df = pd.read_sql('SELECT * FROM {}'.format("customer"), con=db_connection)
        result = df.to_json(orient="index")
        response = json.loads(result)
        return response
    except:
        print('Error:Unable to fetch data.')


@api.post("/customer/{customer}")
def create_customer():
    return 'create_customer in process'


@api.put("/customer/{id}")
def update_cust(id):
    return 'update_cust in process'

@api.delete("/customer/{id}")
def delete_cust_by_id(id):
    print('start request')
    # try:
    #     print('delete')
    #     cursor = mysql_connection.cursor()
    #     cursor.execute("DELETE FROM customer WHERE id_customer={}".format(id))  # Execute SQL Query to detete a record
    #     cu.commit()  # Commit is used for your changes in the database
    #     print('Record deleted successfully...')
    # except:
    #     # rollback used for if any error
    #     mysql_connection.rollback()
    #     print('rollback...')
    # mysql_connection.close()  # Connection Close

# ###################   TEXT    ######################################################################

@api.get("/text/{customerId}/{period}")
def get_text_by_customerId_period(customerId, period):
    return "get_text_by_customerId_period in process"

@api.post("/text/{customerId}")
def create_text(customerId):
    return "create_text in process"

# ###################   FEELING    ######################################################################
@api.get("/feeling/{customerId}/{period}")
def get_avg_feeling_customerId_period(customerId,period):
    return "get_avg_feeling_period in process"

@api.get("/feeling/{period}")
def get_avg_feeling_all_period(period):
    return "get_avg_feeling_all_period in process"