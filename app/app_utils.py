import pandas as pd
import streamlit as st
import requests

from datetime import datetime
from src.start.to_start import db_connection


# #################################################################################""
def display_all_cust():
    """
    request api for the list of all guest
    :return:
    """
    response = requests.get(" http://127.0.0.1:8000/customer")
    if not response:
        st.write('No Data!')
    else:
        j = response.json()
        st.json(j)


def display_cust_by_id(id):
    response = requests.get(" http://127.0.0.1:8000/customer/{}".format(id))
    if not response:
        st.write('No Data!')
    else:
        customer = response.json()
        st.write(customer['name'])


def create_cust():
    input_name = st.text_input('Name:')
    if len(input_name) > 0:
        input_firstname = st.text_input('Firstname:')
        if len(input_firstname) > 0:
            input_information = st.text_input('Information:')
            if len(input_information) > 0:
                if st.button('create customer'):
                    # response = requests.post("http://127.0.0.1:8000/customer/{}".format())
                    response = "create_customer in process"
                    if not response:
                        st.write("not created")
                    else:
                        st.write(response)


def modify_cust(id):
    st.write("modify_cust todo")


def delete_cust_by_id(id):
    print("start1")
    requests.delete("http://127.0.0.1:8000/customer/{}".format(id))


def display_coach_page():
    """
    display the init coach page
    :return:
    """
    selection = st.selectbox("Action", ["", 'display a customer', "create a customer", 'display all customers'])
    if selection == "display a customer":
        input_id = st.number_input('enter the customer id to display')
        if input_id > 0:
            input_id = int(input_id)
            display_cust_by_id(input_id)
    elif selection == "create a customer":
        create_cust()
    elif selection == "display all customers":
        display_all_cust()
    else:
        st.write("choisir tu dois")


def display_cust_page():
    st.write("this is the customer page")


def charge_all_data(table_name):
    df = pd.read_sql('SELECT * FROM {}'.format(table_name), con=db_connection)
    return df


def upload_table(df, table_name):
    df.to_sql(table_name, db_connection, if_exists="replace")
