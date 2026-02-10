from database.supabase_client import supabase
from postgrest.exceptions import APIError


def get_history() -> list[dict]:
    try:
        response = supabase.table("historiques_avant_suivi").select("*").execute()
        return response.data
    except APIError as e:
        print(f"Erreur Supabase : {e.message}")
        return []
    except Exception as e:
        print(f"Exception lors de la récupération : {str(e)}")
        return []

