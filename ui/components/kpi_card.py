import streamlit as st
class KPICard:
    def __init__(self, label, value, icon="📊", color="#2196F3", label_color="#0A273B", currency="€"):
        self.label = label
        self.value = value
        self.icon = icon
        self.color = color
        self.label_color = label_color
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
                background: linear-gradient(135deg, {self.color}, #1976D2);
                padding: 14px;
                border-radius: 14px;
                width: 100%;
                text-align: center;
                box-shadow: 0 6px 14px rgba(0,0,0,0.08);
                margin: 10px 0;
                color: #FFFFFF;
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            ">
            <div style="
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                margin-bottom: 6px;
                color: {self.label_color};
            ">
                <div style="font-size: 18px;">{self.icon}</div>
                <div style="font-size: 14px; font-weight: 500;">{self.label}</div>
            </div>
            <div class="kpi-value-dynamic" style="
                font-size: 26px;
                font-weight: bold;
            ">
                {self.value:,.2f} {self.currency}
            </div>
        </div>
        """
