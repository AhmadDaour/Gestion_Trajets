import streamlit as st
from services.dashboard_service import DashboardService
from ui.components.cards.dashboard_kpi_card import DashboardKPICard
from core.core_ui import UI

def render_dashboard():
    kpis = DashboardService().get_dashboard_kpis()
    kpi_list = [
        ("Chiffre d'affaires", kpis.total_ca, "€", "💰"),
        ("Achat Carburants", kpis.total_carburant, "€", "⛽️"),
        ("Bénéfice brut", kpis.benefice_total, "€", "📈"),
        ("Dernier plein", kpis.dernier_plein, "€", "🛢️"),
        ("Total distance", kpis.total_distance, "km", "🛣️"),
        ("Bénéfice net", kpis.benefice_net, "€", "💰")
    ]
    cols_per_row = 3
    for i in range(0, len(kpi_list), cols_per_row):
        row_kpis = kpi_list[i:i + cols_per_row]
        cols = st.columns(len(row_kpis)) 

        for j, (label, value, unit, icon) in enumerate(row_kpis):
            formatted_value = UI.format_value(value, unit)
            DashboardKPICard(label, formatted_value, icon).render(cols[j])