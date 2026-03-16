from database.trip_repository import TripRepository
import streamlit as st
from st_aggrid import AgGrid

class HistoriquesService:
    def __init__(self):
        self.trip_repo = TripRepository()

    def get_trips(self):
        return self.trip_repo.get_trips()
     
    

