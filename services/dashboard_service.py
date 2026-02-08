from database.trip_repository import TripRepository
from database.fuel_repository import FuelRepository
from utils.calculations import Calculations

class DashboardService:
    def __init__(self):
        self.repo = TripRepository()
        self.fuel_repo = FuelRepository()

    def get_kpis(self):
        trips = self.repo.get_trips()
        fuels = self.fuel_repo.get_fuels()
        total_ca = Calculations.total_CA(trips)
        total_fuels = Calculations.total_fuels(fuels)

        return total_ca, total_fuels, total_ca - total_fuels