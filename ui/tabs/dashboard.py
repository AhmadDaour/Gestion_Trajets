import streamlit as st
from services.dashboard_service import DashboardService
from ui.components.kpi_card import KPICard


def render_dashboard():
    service = DashboardService()
    total_ca, total_fuels, total_benef = service.get_kpis()
    col1, col2, col3 = st.columns(3)

    with col1:
        KPICard(label="Chiffre d'affaires", value=total_ca, icon="💰", background_color="#454748", text_color="#E6F8EDDF").render()
    with col2:
        KPICard(label="Dépenses carburant", value=total_fuels, icon="⛽", background_color="#2196F3", text_color="#F6071B").render()
    with col3:
        KPICard(label="Bénéfices", value=total_benef, icon="📈", background_color="#2196F3", text_color="#29EB07").render()