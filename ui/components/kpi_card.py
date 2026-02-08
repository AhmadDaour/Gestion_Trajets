import streamlit as st

class KPICard:
    def __init__(self, label, value, icon="📊", color="#4CAF50", currency="€"):
        self.label = label
        self.value = value
        self.icon = icon
        self.color = color
        self.currency = currency

    def render(self):
        try:
            st.markdown(self._html(), unsafe_allow_html=True)
        except Exception as e:
            st.error(f"KPI render error: {e}")

    def _html(self):
        return f"""
        <div class="kpi-card"
            style="
                border-left: 6px solid {self.color};
                padding: 12px;
                border-radius: 6px;
                background-color: #f9f9f9;
                width: 100%;
                text-align: center;
            ">
            <div style="display:flex; align-items:center; justify-content: center; gap:8px; margin-bottom:6px;">
                <div class="kpi-icon"
                    style="font-size: 18px;">
                    {self.icon}
                </div>
                <div class="kpi-label"
                    style="font-size: 14px; color: #888;">
                    {self.label}
                </div>
            </div>
            <div class="kpi-value"
                style="font-size: 26px; font-weight: bold;">
                {self.value:,.2f} {self.currency}
            </div>
        </div>
        """
