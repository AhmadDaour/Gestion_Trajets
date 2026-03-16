import streamlit as st
from datetime import datetime

def render_fuel_form():
    with st.form("saisie_plein", clear_on_submit=True):
        prix_total = st.number_input("Prix total (€)", min_value=0.0, format="%.3f", value=None, placeholder="0,000")
        prix_litre = st.number_input("Prix par litre (€)", min_value=0.0, format="%.3f", value=None, placeholder="0,000")
        nb_litre = st.number_input("Nombre de litres (L)", min_value=0.0, format="%.3f", value=None, placeholder="0,000")
        consommation_moyenne_par_km = st.number_input("Consommation moyenne par km (L/km)", min_value=0.0, value=0.053, format="%.3f")
        date = st.date_input("Date", datetime.today())       
        submit = st.form_submit_button("Ajouter le plein")

    if submit:
        return {
            "prix_total": prix_total,
            "date": date,
            "prix_litre": prix_litre,
            "nb_litre": nb_litre,
            "consommation_moyenne_par_km": consommation_moyenne_par_km
        }
    return None
