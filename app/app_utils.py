import pandas as pd
import streamlit as st
import requests


def charge_all_data(db_connection, table_name):
    df = pd.read_sql('SELECT * FROM' + table_name, con=db_connection)
    return df


def upload_table(df, table_name, db_connection):
    df.to_sql(table_name, db_connection, if_exists="replace")

def display_test():
    search_input = st.text_input('test', '')
    if len(search_input) > 0:
        response = requests.get("https://lit-spire-48980.herokuapp.com/{}".format(search_input))
        emotion = response.json()["emotion"]
        st.write(emotion)
        response = requests.get(
            "https://api.giphy.com/v1/gifs/random?api_key=u5zI8PiTKx0y7b6Csh5GmUdhgD0hZ315&tag={}&rating=g".format(
                emotion))
        image_url = response.json()["data"]["image_original_url"]
        st.image(image_url)
