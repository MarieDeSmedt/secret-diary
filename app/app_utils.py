import pandas as pd
import streamlit as st
import requests


def charge_all_data(db_connection, table_name):
    df = pd.read_sql('SELECT * FROM {}'.format(table_name), con=db_connection)
    return df


def upload_table(df, table_name, db_connection):
    df.to_sql(table_name, db_connection, if_exists="replace")


def display_cust_page():
    st.text_input('entrer id customer', '')
    # if len(id) > 0:
    #     customer = requests.get(" http://127.0.0.1:8000/customer/{}".format(id))
    #     name = customer.json()["name"]
    # else:
    #     name = "no id"
    # st.write(name)
    # charger les data necessaire depuis la db



