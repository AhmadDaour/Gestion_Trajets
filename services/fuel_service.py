from datetime import datetime
from models.fuel import Fuel
from database.fuel_repository import FuelRepository

class FuelService:
    def __init__(self, fuel_repository: FuelRepository):
        self.fuel_repository = fuel_repository
    def add_fuel(self, prix_total: float, date: datetime, prix_litre: float, nb_litre: float, consommation_moyenne_par_km: float) -> dict:
        try:
            fuel = Fuel(prix_total=prix_total, date=date, prix_litre=prix_litre, nb_litre=nb_litre, consommation_moyenne_par_km=consommation_moyenne_par_km)
            self.fuel_repository.save(fuel.to_dict())
            return {
                "status": "success",
                "message": "Plein ajouté avec succès !",
                "data": fuel.to_dict()
            }
        except ValueError as ve:
            return {
                "status": "error",
                "message": f"Erreur de validation : {str(ve)}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erreur lors de l'ajout du trajet : {str(e)}"
            }
