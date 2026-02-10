from database.trip_repository import TripRepository
from database.fuel_repository import FuelRepository
from database.historical_repository import HistoricalRepository
from utils.calculations import Calculations

class DashboardService:
    def __init__(self):
        self.repo = TripRepository()
        self.fuel_repo = FuelRepository()
        self.history_repo = HistoricalRepository()

    def get_kpis(self):
        trips = self.repo.get_trips()
        fuels = self.fuel_repo.get_fuels()
        history = self.history_repo.get_totals()
        total_ca = Calculations.total_CA(trips) + history.historique_CA
        total_fuels = Calculations.total_fuels(fuels) + history.historique_carburants

        return total_ca, total_fuels, total_ca - total_fuels