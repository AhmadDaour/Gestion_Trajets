from database.trip_repository import TripRepository
from database.fuel_repository import FuelRepository
from models.services_kpis import ServicesKPIs



class ServicesService:
    def __init__(self):
        self.trip_repo = TripRepository()

    def get_services_kpis(self):
        ca_du_jour = self.trip_repo.get_ca_today()
        return ServicesKPIs(
            ca_du_jour=ca_du_jour
        )