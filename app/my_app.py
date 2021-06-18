import streamlit as st

from main   import db_connection
from app_utils import charge_all_data, upload_table

# ############################################################################################
st.sidebar.markdown("### test d'API")
app = Page()
app.add_page("coach", display_test)
app.run()

#selon la page
table_name = "customer"

# charger les data necessaire depuis la db
df = charge_all_data(db_connection, table_name)

# a la fin faire un save dans la db
upload_table(df, table_name, db_connection)


# ##########################################################################################
