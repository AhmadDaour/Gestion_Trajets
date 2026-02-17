import streamlit as st
from services.dashboard_service import DashboardService
from services.fuel_service import FuelService
from services.trip_service import TripService   
from ui.components.cards.header_card import render_header
from ui.components.cards.tabs_card import pro_tabs
from onglets.sidebar import render_general_form



import streamlit as st

class MainPage:

    def __init__(self):
        self.dashboard_service = DashboardService()
        self.fuel_service = FuelService(fuel_repository=None) 
        self.trip_service = TripService(trip_repository=None) 

    def render(self):
        # Sidebar
        render_general_form()

        # Header
        render_header(
            title="Gestionnaire de Trajets",
            content="Visualiser de façon claire et structurée les infos relatives aux trajets"
        )

        # Tabs
        pro_tabs()