from database.supabase_client import supabase
from datetime import datetime
from postgrest.exceptions import APIError

class TripRepository:
    def save(self, trip_data: dict) -> bool:
        try:
            response = supabase.table("trajets").insert(trip_data).execute()
            return len(response.data) > 0

        except APIError as e:
            print(f"Erreur Supabase : {e.message}")
            return False

        except Exception as e:
            print(f"Exception lors de la sauvegarde : {str(e)}")
            return False

    def get_trips(self) -> list[dict]:
        try:
            response = supabase.table("trajets").select("*").execute()
            return response.data
        except APIError as e:
            print(f"Erreur Supabase : {e.message}")
            return []
        except Exception as e:
            print(f"Exception lors de la récupération : {str(e)}")
            return []

    def get_ca_today(self) -> float:
        try:
            today = datetime.now().date()
            response = supabase.table("trajets").select("prix").gte("date", today).execute()
            return sum(item['prix'] for item in response.data)
        except APIError as e:
            print(f"Erreur Supabase : {e.message}")
            return 0.0
        except Exception as e:
            print(f"Exception lors de la récupération du CA : {str(e)}")
            return 0.0