import streamlit as st
from onglets.dashboard import render_dashboard

def render_tabs():

    tab1, tab2 = st.tabs(["Dashboard", "Historiques"])

    with tab1:
        render_dashboard()

    with tab2:
        st.markdown("### Historiques")
        st.write("À venir : Historique des données et analyses.")
