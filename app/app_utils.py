import pandas as pd
import streamlit as st
import requests
import api.schemas as schemas
from datetime import datetime

from src.start.to_start import db_connection


# ##########################################CUSTOMER#######################################""
def display_cust_by_id(id):
    response = requests.get(" http://127.0.0.1:8000/customer/{}".format(id))
    if not response:
        st.write('No Data!')
    else:
        customer = response.json()
        st.write('Name: ', customer['name'])
        st.write('Firstname: ', customer['firstname'])
        st.write('Information: ', customer['information'])
        st.write('Creation_date: ', customer['creation_date'])


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


def create_cust():
    input_name = st.text_input('Name:')
    if len(input_name) > 0:
        input_firstname = st.text_input('Firstname:')
        if len(input_firstname) > 0:
            input_information = st.text_input('Information:')
            if len(input_information) > 0:
                if st.button('create customer'):
                    customer = {}
                    customer['name'] = input_name
                    customer['firstname'] = input_firstname
                    customer['information'] = input_information
                    customer['creation_date'] = datetime.today().strftime('%Y-%m-%d')

                    response = requests.post("http://127.0.0.1:8000/customer/", json=customer)
                    if not response:
                        st.write("request failed")
                    else:
                        st.write("Customer {} {} is created".format(input_name, input_firstname))


def update_cust_by_id(id):
    response = requests.get(" http://127.0.0.1:8000/customer/{}".format(id))
    if not response:
        st.write('No Data!')
    else:
        old_dcustomer = response.json()
        st.write('Name: ', old_dcustomer['name'])
        st.write('Firstname: ', old_dcustomer['firstname'])
        st.write('Information: ', old_dcustomer['information'])
        st.write('Creation date: ', old_dcustomer['creation_date'])
        st.write('Last modification date: ', old_dcustomer['modification_date'])
    input_name = st.text_input('Update name:')
    input_firstname = st.text_input('Update firstname:')
    input_information = st.text_input('Update information:')
    if st.button('update customer'):
        customer = {}
        if input_name != "":
            customer['name'] = input_name
        else:
            customer['name'] = old_dcustomer['name']

        if input_firstname != "":
            customer['firstname'] = input_firstname
        else:
            customer['firstname'] = old_dcustomer['firstname']

        if input_information != "":
            customer['information'] = input_information
        else:
            customer['information'] = old_dcustomer['information']

        customer['modification_date'] = datetime.today().strftime('%Y-%m-%d')

        response = requests.put("http://127.0.0.1:8000/customer/{}".format(id), json=customer)
        if not response:
            st.write("request failed")
        else:
            st.write("Customer {} {} is updated".format(input_name, input_firstname))


def delete_cust_by_id(id):
    response = requests.get(" http://127.0.0.1:8000/customer/{}".format(id))
    if not response:
        st.write('customex dont exist!')
    else:
        response = requests.delete("http://127.0.0.1:8000/customer/{}".format(id))
        if not response:
            st.write('no response')
        else:
            st.write('customer deleted')


# ############################################DISPLAY######################################"

def display_coach_page():
    selection = st.selectbox("Action",
                             ["Chosse action", "create a customer", 'display a customer', 'display all customers',
                              'delete customer', 'update a customer'], index=0)
    if selection == "display a customer":
        input_id = st.number_input('enter the customer id to display')
        if input_id > 0:
            input_id = int(input_id)
            display_cust_by_id(input_id)
    elif selection == "create a customer":
        create_cust()
    elif selection == "display all customers":
        display_all_cust()
    elif selection == 'delete customer':
        input_id = st.number_input('enter the customer id to delete')
        if input_id > 0:
            input_id = int(input_id)
            delete_cust_by_id(input_id)
    elif selection == 'update a customer':
        input_id = st.number_input('enter the customer id to update')
        if input_id > 0:
            input_id = int(input_id)
            update_cust_by_id(input_id)


def display_cust_page():
    name = st.text_input('Name')
    firstname = st.text_input('Firstname')
    if name and firstname:
        response = requests.get(" http://127.0.0.1:8000/customer/name/{}".format(name))
        if not response:
            st.write('Customer dont exist')
        else:
            customer = response.json()
            selection = st.selectbox("Action",
                                     ["Chosse action", "create a text", "display list of texts"])
            if selection == "create a text":
                create_text(customer['id_customer'])
            if selection == "display list of texts":
                display_all_text(customer['id_customer'])


# ##########################################TEXT##################################################""

def create_text(id_customer: int):
    text = st.text_input('')
    if text:
        if st.button('save text'):
            new_text = {}
            new_text['content'] = text
            new_text['creation_date'] = datetime.today().strftime('%Y-%m-%d')
            new_text['first_feeling '] = "happy"
            new_text['first_pourcentage'] = 50
            new_text['second_feeling'] = "anger"
            new_text['second_pourcentage'] = 30
            new_text['third_feeling'] = "doubt"
            new_text['third_pourcentage'] = 20
            new_text['id_customer'] = id_customer

            response = requests.post("http://127.0.0.1:8000/text/", json=new_text)
            if not response:
                st.write("request failed")
            else:
                st.write("the text is save")


def display_all_text(id_customer: int):
    response = requests.get(" http://127.0.0.1:8000/text/{}".format(id_customer))
    if not response:
        st.write('No Data!')
    else:
        j = response.json()
        st.json(j)
