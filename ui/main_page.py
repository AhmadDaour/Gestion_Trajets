import streamlit as st
from ui.components.header import render_header
from ui.components.pro_tabs import pro_tabs
from onglets.sidebar import render_general_form
from utils.injection_css_global import _inject_global_styles


import streamlit as st

class MainPage:

    def __init__(self):
        _inject_global_styles()

    def render(self):
        # Sidebar
        render_general_form()

        # Header
        render_header()

        # Tabs
        pro_tabs()