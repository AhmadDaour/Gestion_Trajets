import streamlit as st
from services.dashboard_service import DashboardService
from ui.components.cards.kpi_card import KPICard


def render_dashboard():
    kpis = DashboardService().get_kpis()
    col1, col2, col3 = st.columns(3)  
    with col1:
        KPICard("Chiffre d'affaires", kpis.total_ca, "💰").render(col1) 
    with col2:
        KPICard("Total Carburants", kpis.total_carburant, "⛽️").render(col2)
    with col3:
        KPICard("Bénéfices", kpis.benefice_total, "📈").render(col3)