import streamlit as st
from datetime import datetime
from services.trip_service import TripService
from services.fuel_service import FuelService
from database.trip_repository import TripRepository
from database.fuel_repository import FuelRepository

def render_sidebar():
    with st.sidebar:
        st.header("Ajouter un trajet:")
        with st.form("saisie_trajet"):
            distance = st.number_input("Distance (km)", min_value=0.0)
            date = st.date_input("Date", datetime.today())
            prix = st.number_input("Prix (€)", min_value=0.0)
            ajouter_trajet = st.form_submit_button("Ajouter le trajet")

        if ajouter_trajet:
            trip_repository = TripRepository()
            trip_service = TripService(trip_repository)

            result_trajet = trip_service.add_trip(distance=distance, date=date, prix=prix)

            if result_trajet["status"] == "success":
                st.success(result_trajet["message"])
            else:
                st.error(result_trajet["message"])


        st.header("Ajouter un plein:")
        with st.form("saisie_plein"):
            prix_total = st.number_input("Prix total (€)", min_value=0.0)
            date_plein = st.date_input("Date du plein", datetime.today())
            prix_litre = st.number_input("Prix par litre (€)", min_value=0.0)
            nb_litre = st.number_input("Nombre de litres (L)", min_value=0.0)
            consommation_moyenne_par_km = st.number_input("Consommation moyenne par km (L/km)", min_value=0.0)
            ajouter_plein = st.form_submit_button("Ajouter le plein")
        if ajouter_plein:
            fuel_repository = FuelRepository()
            fuel_service = FuelService(fuel_repository)

            result_plein = fuel_service.add_fuel(prix_total=prix_total, date=date_plein, prix_litre=prix_litre, nb_litre=nb_litre, consommation_moyenne_par_km=consommation_moyenne_par_km)

            if result_plein["status"] == "success":
                st.success(result_plein["message"])
            else:
                st.error(result_plein["message"])

    return {"submit_trajet": ajouter_trajet, "submit_plein": ajouter_plein}