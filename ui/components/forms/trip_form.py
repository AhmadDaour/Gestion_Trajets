import streamlit as st
from datetime import datetime

def render_trip_form():
    with st.form("saisie_trajet", clear_on_submit=True):
        distance = st.number_input("Distance (km)", value=None, placeholder="0,00", min_value=0.0, format="%.2f")
        prix = st.number_input("Prix (€)", value=None, placeholder="0,00", min_value=0.0, format="%.2f" )
        date = st.date_input("Date", datetime.today())
        submit = st.form_submit_button("Ajouter le trajet")

    if submit:
        return {
            "distance": distance,
            "date": date,
            "prix": prix
        }
    return None
