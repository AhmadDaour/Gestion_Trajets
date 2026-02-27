import streamlit as st
from ui.components.cards.service_card import service_card   
from services.services_service import ServicesService
def render_services():
    col1, col2, col3 = st.columns(3)
    with col1:
        service_card("CA du jour", "ca_jour", "🚗")
    show_service()

def show_service():
    service_key = st.session_state.get('selected_service')  
    if service_key == "ca_jour":
        kpis = ServicesService().get_services_kpis()
        st.markdown(f"**Chiffre d'affaires du jour :** {kpis.ca_du_jour:.2f} €")