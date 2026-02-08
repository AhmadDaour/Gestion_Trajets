from database.supabase_client import supabase
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

