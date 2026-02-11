import streamlit as st
from services.dashboard_service import DashboardService
from ui.components.kpi_card import KPICard


def render_dashboard():
    kpis = DashboardService().get_kpis()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        KPICard(label="Chiffre d'affaires", value=kpis.total_ca, icon="💰", background_color="#454748", text_color="#E6F8EDDF").render()
    with col2:
        KPICard(label="Dépenses carburant", value=kpis.total_carburant, icon="⛽", background_color="#2196F3", text_color="#F6071B").render()
    with col3:
        KPICard(label="Bénéfices", value=kpis.benefice_total, icon="📈", background_color="#2196F3", text_color="#29EB07").render()
    with col4:
        KPICard(label="Dernier plein", value=kpis.dernier_plein, icon="⛽", background_color="#2196F3", text_color="#E6F8EDDF").render()