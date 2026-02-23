import streamlit as st
from datetime import datetime

def render_trip_form():
    st.markdown(
    """
    <div class="sidebar-form">
        <h3 class="sidebar-form-title">Ajouter un trajet</h3>
    """,
    unsafe_allow_html=True
)
    with st.form("saisie_trajet", clear_on_submit=True):
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
    st.markdown('</div>', unsafe_allow_html=True)
    return None
