import streamlit as st

from page import Page
from start import db_connection
from app_utils import charge_all_data, display_cust_page

# ############################################################################################
st.sidebar.markdown("### first page")

app = Page()
app.add_page("customer", display_cust_page)
# app.add_page("text", display_text_page)
# app.add_page("feeling", display_feeling_page)

current_table_name = st.sidebar.radio('table', ("customer", "text", "feeling"))
if current_table_name == "customer":
    table_name = "customer"
elif current_table_name == "text":
    table_name = "text"
else:
    table_name = "feeling"

app.run()

# charger les data necessaire depuis la db
df = charge_all_data(db_connection, table_name)
# a la fin faire un save dans la db
# upload_table(df, table_name, db_connection)


# ##########################################################################################
