import streamlit as st

def service_card(title: str, key: str, icon: str = "🔧"):
    st.markdown("""
            <style>

            div.stButton > button {
                height: 80px;
                font-size: 18px;
                font-weight: bold;
                border-radius: 12px;
            }

            div.stButton > button:hover {
                background-color: #ff4b4b;
                color: white;
            }

            </style>
            """, unsafe_allow_html=True)
    st.session_state['selected_service'] = None
    clicked = st.button(f"{icon} {title}",
                        key=key, 
                        use_container_width=True
    )
    if clicked:
        st.session_state['selected_service'] = key
