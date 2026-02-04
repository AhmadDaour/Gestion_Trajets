import streamlit as st
from datetime import datetime
from services.trip_service import TripService
from database.trip_repository import TripRepository

def show_form():
    with st.sidebar:
        st.header("Saisie des données du trajet")
        with st.form("saisie_trajet"):
            distance = st.number_input("Distance (km)", min_value=0.0)
            date = st.date_input("Date", datetime.today())
            prix = st.number_input("Prix (€)", min_value=0.0)
            ajouter = st.form_submit_button("Ajouter")

        if ajouter:
            trip_repository = TripRepository()
            trip_service = TripService(trip_repository)

            result = trip_service.add_trip(distance=distance, date=date, prix=prix)

            if result["status"] == "success":
                st.success(result["message"])
            else:
                st.error(result["message"])

    return {"submit": ajouter}
