from database.trip_repository import TripRepository
from database.fuel_repository import FuelRepository
from database.historical_repository import HistoricalRepository
from utils.calculations import Calculations
from models.dashboard_kpis import DashboardKPIs

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
        dernier_plein = self.fuel_repo.get_last_fuel().prix_total

        return DashboardKPIs(
            total_ca=total_ca,
            total_carburant=total_fuels,
            benefice_total=total_ca - total_fuels,
            dernier_plein=dernier_plein
        )