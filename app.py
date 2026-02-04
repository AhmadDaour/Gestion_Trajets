import streamlit as st
import sys 
from ui.header import header
from ui.sidebar import show_form

sys.dont_write_bytecode = True

st.set_page_config(
    page_title="Gestionnaire de Trajets",
    page_icon="🚗",
    layout="wide"
)

# show header
header()

# show sidebar
form_data = show_form()


