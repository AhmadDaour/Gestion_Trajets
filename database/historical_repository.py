from database.supabase_client import supabase
from postgrest.exceptions import APIError
from models.historical import HistoricalTotals


class HistoricalRepository:

    @staticmethod
    def get_totals() -> HistoricalTotals:
        try:
            response = supabase.table("historiques_avant_suivi").select(
                "historique_CA, historique_carburants"
            ).execute()

            rows = response.data or []

            total_ca = sum(float(row.get("historique_CA", 0)) for row in rows)
            total_carburant = sum(float(row.get("historique_carburants", 0)) for row in rows)

            return HistoricalTotals(
                historique_CA=total_ca,
                historique_carburants=total_carburant
            )

        except APIError as e:
            print(f"Erreur Supabase : {e.message}")
            return HistoricalTotals()
        except Exception as e:
            print(f"Exception : {str(e)}")
            return HistoricalTotals()

