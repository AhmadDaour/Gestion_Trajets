import streamlit as st
import uuid

class KPICard:
    def __init__(
        self,
        label: str,
        value: float,
        icon: str = "📊",
        background_color: str = "#2196F3",
        text_color: str = "#FFFFFF",
        border_radius: int = 18,
        height: int = 120,
        currency: str = "€",
        border_color: str = "#1565C0",
    ):
        self.label = label
        self.value = value
        self.icon = icon
        self.background_color = background_color
        self.text_color = text_color
        self.border_radius = border_radius
        self.height = height
        self.currency = currency
        self.border_color = border_color
        self.unique_id = f"kpi-card-{uuid.uuid4().hex[:8]}"

    def render(self, col=None):
        """
        Affiche la carte KPI dans une colonne Streamlit.

        Args:
            col: Objet colonne Streamlit (ex: `st.columns([1, 1])[0]`).
                 Si None, la carte occupera toute la largeur disponible.
        """
        try:
            # Injection du CSS avec une largeur à 100%
            st.markdown(
                f"""
                <style>
                .{self.unique_id} {{
                    background-color: {self.background_color} !important;
                    color: {self.text_color} !important;
                    padding: 16px !important;
                    border-radius: {self.border_radius}px !important;
                    width: 100% !important;  /* Occupe toute la largeur */
                    height: {self.height}px !important;
                    display: flex !important;
                    flex-direction: column !important;
                    justify-content: center !important;
                    align-items: center !important;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
                    margin: 10px auto !important;
                    font-family: sans-serif !important;
                    border: 1px solid {self.border_color} !important;
                    overflow: hidden !important;
                    box-sizing: border-box !important;  /* Inclut le padding dans la largeur */
                }}
                .{self.unique_id} .kpi-label {{
                    display: flex !important;
                    align-items: center !important;
                    justify-content: center !important;
                    gap: 8px !important;
                    margin-bottom: 10px !important;
                    font-size: 16px !important;
                    font-weight: 500 !important;
                }}
                .{self.unique_id} .kpi-value {{
                    font-size: 24px !important;
                    font-weight: bold !important;
                }}
                </style>
                """,
                unsafe_allow_html=True,
            )

            # Si une colonne est fournie, afficher dans cette colonne
            if col:
                with col:
                    st.markdown(
                        f"""
                        <div class="{self.unique_id}">
                            <div class="kpi-label">
                                {self.icon} <span>{self.label}</span>
                            </div>
                            <div class="kpi-value">
                                {self.value:,.2f} {self.currency}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            else:
                # Sinon, afficher en pleine largeur
                st.markdown(
                    f"""
                    <div class="{self.unique_id}">
                        <div class="kpi-label">
                            {self.icon} <span>{self.label}</span>
                        </div>
                        <div class="kpi-value">
                            {self.value:,.2f} {self.currency}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        except Exception as e:
            st.error(f"Erreur lors du rendu du KPI: {e}")
