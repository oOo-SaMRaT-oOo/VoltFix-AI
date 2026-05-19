import streamlit as st

def make_page_nice():
    st.set_page_config(
        page_title="VoltFix : AI ",
        layout="wide",  
        initial_sidebar_state="expanded"
    )

    st.markdown("""
    <style>
        [data-testid="stMainBlockContainer"] {
            max-width: 800px !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            margin: 0 auto !important;
        }
    </style>
    """, unsafe_allow_html=True)