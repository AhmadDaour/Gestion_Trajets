from Services.utils import supabase
import pandas as pd
import sys
sys.dont_write_bytecode = True

class CrudTrip:

    def Create_Trips(self, form_data):
        """
        Ajoute un trajet dans la base de données Supabase.
        """
        distance = form_data["distance"]
        prix = form_data["prix"]
        date = form_data["date"]
        
        # Calculs automatiques
        cout_par_km = 0.5  # Coût fixe par km (à ajuster selon besoin)
        benefice = prix - (distance * cout_par_km)
        
        # Validation des données
        if distance <= 0:
            raise ValueError("La distance doit être supérieure à 0.")
        if prix <= 0:
            raise ValueError("Le prix doit être supérieur à 0.")
        if not date:
            raise ValueError("La date est invalide.")
        if benefice < 0:
            raise ValueError("Le bénéfice ne peut pas être négatif.")
        if cout_par_km <= 0:
            raise ValueError("Le coût par kilomètre doit être supérieur à 0.")

        # Insertion dans Supabase
        try:
            data = {
                "distance": distance,
                "prix": prix,
                "date": str(date),  # Convertir date en string si nécessaire
                "benefice": benefice,
                "cout_par_km": cout_par_km
            }
            response = supabase.table("trajets").insert(data).execute()
            print("Trajet ajouté avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'ajout du trajet : {str(e)}")
            raise

    def Read_Trips(self, limit=None, offset=0):
        """
        Récupère les trajets sous forme de DataFrame avec pagination.
        
        :param limit: Nombre maximum de trajets à récupérer (None pour tout récupérer).
        :param offset: Décalage pour la pagination.
        :return: DataFrame contenant les trajets.
        """
        try:
            query = supabase.table("trajets").select("*").order("date", desc=True)
            if limit is not None:
                query = query.range(offset, offset + limit - 1)
            response = query.execute()
            trajets = response.data
            df = pd.DataFrame(trajets)
            return df
        except Exception as e:
            print(f"Erreur lors de la récupération des trajets : {str(e)}")
            raise