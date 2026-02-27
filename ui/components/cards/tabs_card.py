import streamlit as st
from onglets.dashboard import render_dashboard
from onglets.services import render_services

def render_tabs():

    tab1, tab2 = st.tabs(["Dashboard", "Services"])

    with tab1:
        render_dashboard()

    with tab2:
        render_services()