import streamlit as st
from datetime import datetime

def render_trip_form():
    with st.form("saisie_trajet"):
        distance = st.number_input("Distance (km)", min_value=0.0)
        date = st.date_input("Date", datetime.today())
        prix = st.number_input("Prix (€)", min_value=0.0)
        submit = st.form_submit_button("Ajouter le trajet")

    if submit:
        return {
            "distance": distance,
            "date": date,
            "prix": prix
        }

    return None
