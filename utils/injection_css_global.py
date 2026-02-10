import streamlit as st

def _inject_global_styles():
    st.markdown("""
    <style>
    @media (prefers-color-scheme: light) {
    .kpi-value-dynamic {
        color: #000000 !important;
    }
}
    @media (prefers-color-scheme: dark) {
        .kpi-value-dynamic {
            color: #FFFFFF !important;
        }
    }
                
    /* Padding global page */
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 1rem !important;
    }

    /* Espace sous header */
    h1 {
        margin-bottom: 0.25rem !important;
    }

    /* Rapproche les tabs */
    .stTabs {
        margin-top: -95px !important;
    }
    </style>
    """, unsafe_allow_html=True)

