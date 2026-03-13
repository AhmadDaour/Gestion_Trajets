import streamlit as st

def service_card(title: str, key: str, icon: str = "🔧"):
    st.session_state['selected_service'] = None
    clicked = st.button(f"{icon} {title}",
                        key=key, 
                        use_container_width=True
    )
    if clicked:
        st.session_state['selected_service'] = key