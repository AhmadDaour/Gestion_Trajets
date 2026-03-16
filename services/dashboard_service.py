from database.trip_repository import TripRepository
from database.fuel_repository import FuelRepository
from database.historical_repository import HistoricalRepository
from utils.calculations import Calculations
from models.dashboard_kpis import DashboardKPIs

class DashboardService:
    def __init__(self):
        self.trip_repo = TripRepository()
        self.fuel_repo = FuelRepository()
        self.history_repo = HistoricalRepository()

    def get_dashboard_kpis(self):
        trips = self.trip_repo.get_trips()
        fuels = self.fuel_repo.get_fuels()
        history = self.history_repo.get_totals()
        total_ca = Calculations.total_CA(trips) + history.historique_CA
        total_fuels = Calculations.total_fuels(fuels) + history.historique_carburants
        dernier_plein = self.fuel_repo.get_last_fuel().prix_total
        total_distance = Calculations.total_distance(trips)
        benefice_net = Calculations.benefice_net(trips)
        ca_jour = self.trip_repo.get_ca_today()
        distance_jour = self.trip_repo.get_distance_today()
        benefice_net_jour = self.trip_repo.get_profit_today()
        return DashboardKPIs(
            total_ca=total_ca,
            total_carburant=total_fuels,
            benefice_total=total_ca - total_fuels,
            dernier_plein=dernier_plein,
            total_distance=total_distance,
            benefice_net=benefice_net,
            ca_du_jour=ca_jour,
            distance_du_jour=distance_jour,
            benefice_net_du_jour=benefice_net_jour
        )