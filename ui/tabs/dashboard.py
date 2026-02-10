import streamlit as st
from services.dashboard_service import DashboardService
from ui.components.kpi_card import KPICard


def render_dashboard():
    service = DashboardService()
    total_ca, total_fuels, total_benef = service.get_kpis()
    col1, col2, col3 = st.columns(3)

    with col1:
        KPICard("Chiffre d'affaires", total_ca, "💰", "#06131F", label_color="#079FEB").render()

    with col2:
        KPICard("Dépenses carburant", total_fuels, "⛽", "#2196F3", label_color="#F6071B").render()

    with col3:
        KPICard("Bénéfices", total_benef, "📈", "#2196F3", label_color="#29EB07").render()