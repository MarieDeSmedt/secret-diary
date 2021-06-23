import pandas as pd
import streamlit as st
import requests
import json
from src.start.to_start import db_connection


# #################################################################################""

def display_coach_page():
    st.write("this is the customer page")
    selection = st.selectbox("Action", ["", 'afficher un client', 'afficher tous les clients'])
    if selection == "afficher un client":
        st.write("ok")
    elif selection == "afficher tous les clients":
        response = requests.get(" http://127.0.0.1:8000/customer")
        if not response:
            st.write('No Data!')
        else:
            j = response.json()
            st.write(j['0']['name'])
    else:
        st.write("")


def display_cust_page():
    st.write("this is the coach page")


def charge_all_data(table_name):
    df = pd.read_sql('SELECT * FROM {}'.format(table_name), con=db_connection)
    return df


def upload_table(df, table_name):
    df.to_sql(table_name, db_connection, if_exists="replace")
