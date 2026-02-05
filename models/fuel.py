import sys
from database.supabase_client import supabase  
sys.dont_write_bytecode = True

class Fuel:
    def __init__(self, prix_total, date, prix_litre, nb_litre, consommation_moyenne_par_km):
        if prix_total < 0:
            raise ValueError("Le prix total doit être supérieur à 0.")
        if not date:
            raise ValueError("La date est requise.")
        if prix_litre <= 0:
            raise ValueError("Le prix du litre doit être supérieur à 0.")
        if nb_litre <= 0:
            raise ValueError("Le nombre de litres doit être supérieur à 0.")
        if consommation_moyenne_par_km <= 0:
            raise ValueError("La consommation moyenne par km doit être supérieure à 0.")
        
        
        self.prix_total = prix_total
        self.date = date
        self.prix_litre = prix_litre
        self.nb_litre = nb_litre
        self.consommation_moyenne_par_km = consommation_moyenne_par_km

    def to_dict(self):
        return {
            "prix_total": self.prix_total,
            "date": str(self.date), 
            "prix_litre": self.prix_litre,
            "nb_litre": self.nb_litre,
            "consommation_moyenne_par_km": self.consommation_moyenne_par_km
        }
