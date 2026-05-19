import streamlit as st
from functions.styling_used import header_text,subheader_text,normal_text,draw_glowing_line,paragraph_header_text
from functions.page_layout import make_page_nice

def write_system_objectives():
    make_page_nice()
    header_text("VoltFix : AI")
    st.markdown("<br>",unsafe_allow_html=True)
    sub_text = "~ Capture The Microsecond Chaos !"
    subheader_text(sub_text)
    draw_glowing_line()

    paragraph_header_text("System Objectives :")
    st.write("---")

    text = "~ Neural Fault Isolation :" 
    normal_text(text)
    text = "To classify complex electrical network anomalies " \
        "and path-to-ground faults using high-precision machine learning " \
        "architectures, achieving localized trip execution across the discrete " \
        "microgrid matrix."
    normal_text(text)
    st.write("---")

    text = "~ Transient Intelligence :"
    normal_text(text)
    text = "To monitor granular sub-cycle disturbances—capturing " \
        "unbalanced sequences, wave distortions, and RMS collapse—to identify the " \
        "exact structural heartbeat of grid infrastructure with microsecond accuracy."
    normal_text(text)
    st.write("---")

    text = "~ Cognitive Autonomous Telemetry :"
    normal_text(text)
    text = "To bridge the gap between raw power surges " \
        "and human overview by transforming invisible high-speed fault streams into " \
        "a high-fidelity visual narrative, empowering instantaneous and predictive " \
        "breakers coordination."
    normal_text(text)
    draw_glowing_line()

    normal_text("~ By Samrat Malla")