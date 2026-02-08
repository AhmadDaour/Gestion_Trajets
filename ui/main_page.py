import streamlit as st
from ui.components.header import render_header
from ui.components.pro_tabs import pro_tabs
from ui.sidebar import render_sidebar
from utils.injection_css_global import _inject_global_styles


import streamlit as st

class MainPage:

    def __init__(self):
        _inject_global_styles()

    def render(self):
        # Sidebar
        render_sidebar()

        # Header
        render_header()

        # Tabs
        pro_tabs()