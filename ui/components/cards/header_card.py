import streamlit as st

def render_header(title: str, content: str):
    st.markdown(f"""
    <div class="header-container">
        <div class="header-card">
            <div class="header-card-title">{title}</div>
            <div class="header-card-content">{content}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)