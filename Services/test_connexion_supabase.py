from Services.utils import supabase
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def afficher_trajets(limite: int = 5) -> None:
    """Affiche les trajets depuis Supabase avec gestion d'erreurs."""
    try:
        response = supabase.table("trajets").select("*").limit(limite).execute()
        
        if not response.data:
            logger.warning("⚠️ Aucune donnée trouvée dans la table 'trajets'")
            return
        
        df = pd.DataFrame(response.data)
        
        print("\n" + "="*80)
        print("📊 LES TRAJETS RÉCENTS")
        print("="*80 + "\n")
        print(df.to_string(index=False))
        print("\n" + "="*80)
        print(f"✅ Total: {len(df)} trajets | Distance moy: {df['distance'].mean():.1f} km")
        print(f"💰 Prix moyen: {df['prix'].mean():.2f}€ | Bénéfice total: {df['benefice'].sum():.2f}€")
        print("="*80 + "\n")
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de la récupération des données: {e}")
        raise

if __name__ == "__main__":
    afficher_trajets()

