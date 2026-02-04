from datetime import datetime
from models.trip import Trip
from database.trip_repository import TripRepository

class TripService:
    def __init__(self, trip_repository: TripRepository):
        self.trip_repository = trip_repository

    def add_trip(self, distance: float, date: datetime, prix: float) -> dict:
        try:
            trip = Trip(distance=distance, prix=prix, date=date)
            self.trip_repository.save(trip.to_dict())
            return {
                "status": "success",
                "message": "Trajet ajouté avec succès !",
                "data": trip.to_dict()
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
