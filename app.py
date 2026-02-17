import streamlit as st
import sys 
from theme.inject_css import inject_css
from ui.main_page import MainPage

sys.dont_write_bytecode = True
st.set_page_config(
    page_title="Gestionnaire de Trajets",
    page_icon="🚗",
    layout="wide"
)

inject_css()
main_page = MainPage()
main_page.render()


