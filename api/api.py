import pandas as pd
import json
from datetime import datetime

from fastapi import FastAPI
from src.start.to_start import db_connection, mysql_connection
from src.utils.mysql_utils import connect_to_mysql


api = FastAPI()

def request_to_db(request):

# ###################   CUSTOMER    ######################################################################

@api.get("/customer/{id}")
def get_cust_by_id(id):
    """
    return a customer choosed by id
    :param id: id  (int) of the choosen customer
    :return: a dict (one customer)
    """
    df = pd.read_sql('SELECT * FROM customer WHERE id_customer = {}'.format(id), con=db_connection)
    result = df.to_json(orient="index")
    response = json.loads(result)
    return response


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



@api.post("/customer/{cust_info}")
def create_customer(cust_info):
    print('start')
    if len(cust_info)>0:
        name = cust_info[0]
        firstname = cust_info[1]
        information = cust_info[2]
        creation_date = datetime.date(datetime.now())

    request = "insert into customer(name,firstname, information, creation_date)"+\
              " values({},{},{},{})".format(name,firstname, information, creation_date)

    mysql_connection = connect_to_mysql()
    mycursor = mysql_connection.cursor()  # cursor() method create a cursor object
    try:
        # Execute SQL Query to insert record
        mycursor.execute(request)
        db_connection.commit()  # Commit is used for your changes in the database
        print('Record inserted successfully...')
    except:
        # rollback used for if any error
        db_connection.rollback()
    db_connection.close()  # Connection Close

@api.put("/customer/{id}")

@api.delete("/customer/{id}")
def delete_cust_by_id(id):
    print('start')
    #
    # try:
    #     print('delete')
    #     cursor = mysql_connection.cursor()
    #     cursor.execute("DELETE FROM customer WHERE id_customer={}".format(id))  # Execute SQL Query to detete a record
    #     db_connection.commit()  # Commit is used for your changes in the database
    #     print('Record deleted successfully...')
    # except:
    #     # rollback used for if any error
    #     db_connection.rollback()
    #     print('rollback...')
    # mysql_connection.close()  # Connection Close



# ###################   TEXT    ######################################################################

# ###################   FEELING    ######################################################################
