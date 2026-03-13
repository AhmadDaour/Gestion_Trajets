import streamlit as st

class DashboardKPICard:
    def __init__(self, label: str, value: str, icon: str = "📊"):
        self.label = label
        self.value = value
        self.icon = icon

    def render(self, col=None):
        html = f"""
        <div class="kpi-card">
            <div class="kpi-label">
                {self.icon} <span>{self.label}</span>
            </div>
            <div class="kpi-value">
                {self.value}
            </div>
        </div>
        """

        if col:
            with col:
                st.markdown(html, unsafe_allow_html=True)
        else:
            st.markdown(html, unsafe_allow_html=True)