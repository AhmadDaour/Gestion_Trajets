import streamlit as st
from services.dashboard_service import DashboardService
from ui.components.kpi_card import KPICard
from utils.injection_css_global import _inject_cards_styles


def render_dashboard():
    _inject_cards_styles()
    service = DashboardService()
    total_ca, total_fuels, total_benef = service.get_kpis()
    col1, col2, col3 = st.columns(3)

    with col1:
        KPICard("Chiffre d'affaires", total_ca, "💰", "#4CAF50").render()

    with col2:
        KPICard("Dépenses carburant", total_fuels, "⛽", "#F44336").render()

    with col3:
        KPICard("Bénéfices", total_benef, "📈", "#2196F3").render()