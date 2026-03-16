import streamlit as st
from onglets.dashboard import render_dashboard
from onglets.historiques import render_historiques

def render_tabs():

    tab1, tab2 = st.tabs(["Dashboard", "Historiques des trajets"])

    with tab1:
        render_dashboard()

    with tab2:
        render_historiques()