import streamlit as st
from ui.components.header import render_header
from ui.sidebar import render_sidebar

class MainPage:
    def render(self):
        # show sidebar
        render_sidebar()

        # show header
        render_header()