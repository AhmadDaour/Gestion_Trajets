# Importation des bibliothèques nécessaires'
import streamlit as st
import os
import sys
from datetime import datetime
from Services.Styles import Style    
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from onglets.CRUD_Trips import CrudTrip


sys.dont_write_bytecode = True

st.set_page_config(
    page_title="Gestionnaire de Trajets",
    page_icon="🚗",
    layout="wide"
)



# Affichage du titre de l'application
Style.afficher_titre_application()

Style.ajouter_separateur()

Style.afficher_formulaire_saisie()
