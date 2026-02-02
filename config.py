# config.py
from dotenv import load_dotenv
import os

# Charger le fichier .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
