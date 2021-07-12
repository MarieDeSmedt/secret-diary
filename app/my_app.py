import streamlit as st

import sys
sys.path.insert(0, "/home/apprenant/PycharmProjects/secret-diary")

from app_utils import display_cust_page, display_coach_page
from page import Page

# ############################################################################################

# initiate the home page with the sidebar options

st.sidebar.markdown("### first page")

app = Page()
app.add_page("coach", display_coach_page)
app.add_page("customer", display_cust_page)
app.run()


# ##########################################################################################
