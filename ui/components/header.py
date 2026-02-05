import streamlit as st
import streamlit.components.v1 as components

def render_header():
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