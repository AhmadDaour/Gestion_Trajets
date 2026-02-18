import streamlit as st
from datetime import datetime

def render_fuel_form():
    st.markdown(
    """
    <div class="sidebar-form">
        <h3 class="sidebar-form-title">Ajouter un plein</h3>
    """,
    unsafe_allow_html=True
)
    with st.form("saisie_plein"):
        prix_total = st.number_input("Prix total (€)", min_value=0.0)
        date = st.date_input("Date du plein", datetime.today())
        prix_litre = st.number_input("Prix par litre (€)", min_value=0.0)
        nb_litre = st.number_input("Nombre de litres (L)", min_value=0.0)
        consommation = st.number_input("Consommation moyenne par km (L/km)", min_value=0.0)
        submit = st.form_submit_button("Ajouter le plein")

    if submit:
        return {
            "prix_total": prix_total,
            "date": date,
            "prix_litre": prix_litre,
            "nb_litre": nb_litre,
            "consommation": consommation
        }

    st.markdown('</div>', unsafe_allow_html=True)
    return None
