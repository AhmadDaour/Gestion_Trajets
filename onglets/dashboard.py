import streamlit as st
from services.dashboard_service import DashboardService
from ui.components.cards.kpi_card import KPICard
from core.core_ui import UI


def render_dashboard():
    kpis = DashboardService().get_kpis()
    kpi_list = [
        ("Chiffre d'affaires", kpis.total_ca, "€", "💰"),
        ("Total Carburants", kpis.total_carburant, "€", "⛽️"),
        ("Bénéfices", kpis.benefice_total, "€", "📈")
    ]
    cols = st.columns(len(kpi_list))

    for i, (label, value, unit, icon) in enumerate(kpi_list):
        formatted_value = UI.format_value(value, unit)  # formatage FR centralisé
        KPICard(label, formatted_value, icon).render(cols[i])