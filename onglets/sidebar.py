from ui.components.forms.trip_form  import render_trip_form
from ui.components.forms.fuel_form import render_fuel_form
from services.trip_service import TripService
from services.fuel_service import FuelService
from database.trip_repository import TripRepository
from database.fuel_repository import FuelRepository
import streamlit as st

def render_general_form():

    with st.sidebar:

        trip_data = render_trip_form()

        if trip_data:
            service = TripService(TripRepository())
            result = service.add_trip(**trip_data)

            if result["status"] == "success":
                st.success(result["message"])
            else:
                st.error(result["message"])

        fuel_data = render_fuel_form()

        if fuel_data:
            service = FuelService(FuelRepository())
            result = service.add_fuel(**fuel_data)

            if result["status"] == "success":
                st.success(result["message"])
            else:
                st.error(result["message"])
