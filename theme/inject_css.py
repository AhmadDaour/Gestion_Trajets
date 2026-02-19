import streamlit as st
from pathlib import Path


def inject_css():

    css_dir = Path("theme")

    css = ""

    for file in sorted(css_dir.glob("*.css")):

        css += file.read_text() + "\n"


    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )
