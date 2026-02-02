import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

class Style:
    @staticmethod
    def afficher_titre_application():
        components.html("""
        <style>
        .card {
            border-top: 7px solid #3B82F6;
            padding: 1rem;
            border-radius: 10px;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 600px;  /* Limite la largeur pour éviter les coupures */
            margin: 0 auto;    /* Centre horizontalement */
        }
        .card-title {
            font-size: 1.8rem;
            font-weight: bold;
            color: #2563EB;
        }
        .card-content {
            margin-top: 1rem;
            color: #4B5563;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 2rem;
            padding: 0 1rem;  /* Ajoute un padding pour éviter les bords */
        }
        </style>
        <div class="container">
            <div class="card">
                <div class="card-title">Gestionnaire de Trajets</div>
                <div class="card-content">Visualiser de façon claire et structurée les infos relatives aux trajets</div>
            </div>
        </div>
        """, height=200)
    @staticmethod
    def afficher_formulaire_saisie():
        with st.sidebar:
            st.header("Saisie des données du trajet")
            with st.form("saisie_trajet"):
                distance = st.number_input("Distance (km)", min_value=0.0)
                date = st.date_input("Date", datetime.today())
                prix = st.number_input("Prix (€)", min_value=0.0)
                ajouter = st.form_submit_button("Ajouter")
            if ajouter:
                return {"distance": distance, "date": date, "prix": prix, "submit": True}
        return {"submit": False}
    @staticmethod
    def ajouter_separateur():
        st.markdown('</div><div class="form-section">', unsafe_allow_html=True)
