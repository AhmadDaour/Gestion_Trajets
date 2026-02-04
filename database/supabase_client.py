import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les clés depuis les variables d'environnement
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Validation : s'assurer que les clés sont présentes
if not SUPABASE_URL:
    raise ValueError("SUPABASE_URL n'est pas défini dans le fichier .env")
if not SUPABASE_KEY:
    raise ValueError("SUPABASE_ANON_KEY n'est pas défini dans le fichier .env")

# Créer le client Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Exporter le client pour utilisation dans d'autres modules
__all__ = ["supabase"]
