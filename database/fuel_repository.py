from database.supabase_client import supabase
from models.fuel import Fuel
from postgrest.exceptions import APIError

class FuelRepository:
    def save(self, fuel_data: dict) -> bool:
        try:
            response = supabase.table("carburants").insert(fuel_data).execute()
            return len(response.data) > 0

        except APIError as e:
            print(f"Erreur Supabase : {e.message}")
            return False

        except Exception as e:
            print(f"Exception lors de la sauvegarde : {str(e)}")
            return False
        
    def get_fuels(self) -> list[dict]:
        try:
            response = supabase.table("carburants").select("*").execute()
            return response.data if response.data else []

        except APIError as e:
            print(f"Erreur Supabase : {e.message}")
            return []

        except Exception as e:
            print(f"Exception lors de la récupération : {str(e)}")
            return []
        
    def get_last_fuel(self):
        response = (
            supabase.table("fuels")
            .select("*")
            .order("date", desc=True)
            .order("id", desc=True)
            .limit(1)
            .execute()
        )

        data = response.data

        if not data:
            return None

        row = data[0]

        return Fuel(
            prix_total=row["prix_total"],
            date=row["date"],
            prix_litre=row["prix_litre"],
            nb_litre=row["nb_litre"],
            consommation_moyenne_par_km=row["consommation_moyenne_par_km"],
        )

