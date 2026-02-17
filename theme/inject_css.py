import streamlit as st
def inject_css():

    files = [
        "theme/base.css",
        "theme/cards.css",
        "theme/variables.css",
        "theme/sidebar.css",
        "theme/tabs.css",
    ]

    for file in files:

        with open(file) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
