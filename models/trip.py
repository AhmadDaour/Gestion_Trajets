import sys
from database.supabase_client import supabase  
sys.dont_write_bytecode = True

class Trip:
    def __init__(self, distance, prix, date):
        if distance <= 0:
            raise ValueError("La distance doit être supérieure à 0.")
        if prix <= 0:
            raise ValueError("Le prix doit être supérieur à 0.")
        if not date:
            raise ValueError("La date est requise.")
        
        self.distance = distance
        self.prix = prix
        self.date = date
        self.cost_per_km = self._get_cost_per_km()  
        self.benefit = self._calculate_benefit()  
          

    def _get_cost_per_km(self):
        try:
            response = supabase.table("carburants").select("prix_litre, consommation_moyenne_par_km").order("id", desc=True).limit(1).execute()
            if response.data:
                prix_litre = response.data[0]["prix_litre"]
                consommation_moyenne_par_km = response.data[0]["consommation_moyenne_par_km"]
                cost_per_km = prix_litre * consommation_moyenne_par_km
                return cost_per_km
            else:
                raise ValueError("Aucune donnée de carburant trouvée dans Supabase.")
        except Exception as e:
            print(f"Erreur lors de la récupération du coût par km : {str(e)}")
            return 0.1

    def _calculate_benefit(self):
        return self.prix - (self.cost_per_km * self.distance)

    def to_dict(self):
        return {
            "distance": self.distance,
            "prix": self.prix,
            "date": str(self.date), 
            "benefice": self.benefit,
            "cout_par_km": self.cost_per_km
        }
