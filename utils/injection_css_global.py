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

    .kpi-card {
        position: relative;
        padding: 24px;
        border-radius: 20px;
        background: linear-gradient(145deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        transition: all 0.25s ease;
        overflow: hidden;
        height: 170px;
    }

    .kpi-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 14px 40px rgba(0,0,0,0.35);
    }

    .kpi-glow {
        position: absolute;
        width: 120px;
        height: 120px;
        background: radial-gradient(circle, var(--glow-color) 0%, transparent 70%);
        top: -30px;
        right: -30px;
        opacity: 0.25;
    }

    .kpi-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .kpi-icon {
        font-size: 30px;
        opacity: 0.9;
    }

    .kpi-label {
        font-size: 13px;
        opacity: 0.6;
        letter-spacing: 0.5px;
    }

    .kpi-value {
        font-size: 30px;
        font-weight: 700;
        margin-top: 6px;
    }

    .kpi-badge {
        font-size: 12px;
        padding: 4px 10px;
        border-radius: 999px;
        font-weight: 600;
    }

    .badge-up {
        background: rgba(76, 175, 80, 0.15);
        color: #4CAF50;
    }

    .badge-down {
        background: rgba(244, 67, 54, 0.15);
        color: #F44336;
    }

    </style>
    """, unsafe_allow_html=True)

