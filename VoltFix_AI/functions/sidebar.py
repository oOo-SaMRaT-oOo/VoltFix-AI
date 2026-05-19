import streamlit as st

def custom_sidebar():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&display=swap');

        /* =========================================================
            REMOVE STREAMLIT DEFAULT ELEMENTS & "KEYBOARD" TEXT
        ========================================================= */
        
        button[kind="header"],
        [data-testid="stSidebarNavCollapseButton"],
        [data-testid="collapsedControl"],
        [data-testid="baseButton-header"],
        [data-testid="stSidebarCollapseButton"],
        header[data-testid="stHeader"],
        header[data-testid="stSidebarHeader"],
        div[role="tooltip"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Strong removal of "Keyboard" / shortcut text */
        [data-testid="stSidebar"] button span,
        [data-testid="stSidebar"] div[class*="st-key"],
        [data-testid="stSidebar"] span[class*="keyboard"],
        [data-testid="stSidebar"] [class*="shortcut"],
        [data-testid="stSidebar"] [data-testid*="button"] span,
        .st-emotion-cache-1avcm0n,
        .st-emotion-cache-z5fcl4,
        .st-emotion-cache-79elbk,
        .st-emotion-cache-12fmjuu,
        .st-emotion-cache-1wbqy5l {
            display: none !important;
            visibility: hidden !important;
            font-size: 0 !important;
            width: 0 !important;
            height: 0 !important;
            overflow: hidden !important;
        }

        /* =========================================================
            SIDEBAR BASE STYLING
        ========================================================= */

        [data-testid="stSidebar"] {
            width: 80px !important;
            min-width: 80px !important;
            background: rgba(12, 27, 51, 0.92) !important;
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(0, 183, 255, 0.35);
            overflow-x: hidden !important;
            transition: width 0.35s ease, 
                        min-width 0.35s ease, 
                        box-shadow 0.35s ease;
        }

        /* =========================================================
            EXPAND ON HOVER
        ========================================================= */

        [data-testid="stSidebar"]:hover {
            width: 300px !important;
            min-width: 300px !important;
            box-shadow: 0 0 25px rgba(0,183,255,0.35),
                        0 0 50px rgba(0,183,255,0.15);
        }

        /* =========================================================
            GLOBAL FONT & COLOR
        ========================================================= */

        [data-testid="stSidebar"] * {
            font-family: 'Dancing Script', cursive !important;
            color: #a0e7ff !important;
        }

        /* =========================================================
            HIDE WIDGET LABELS
        ========================================================= */

        [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
            display: none !important;
        }

        /* =========================================================
            RADIO BUTTON STYLING
        ========================================================= */

        .stRadio > div {
            gap: 18px;
            padding-top: 20px;
        }

        .stRadio label {
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            width: 240px !important;
            min-height: 70px !important;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(0,183,255,0.15);
            backdrop-filter: blur(10px);
            padding: 12px 18px;
            border-radius: 16px;
            transition: all 0.25s ease;
            cursor: pointer;
            margin-bottom: 12px;
            box-sizing: border-box !important;
        }

        .stRadio label:hover {
            transform: translateX(8px) scale(1.06);
            background: rgba(0,183,255,0.12);
            border: 1px solid rgba(0,183,255,0.5);
            box-shadow: 0 0 15px rgba(0,183,255,0.45),
                        0 0 30px rgba(0,183,255,0.2);
        }

        .stRadio label:has(input:checked) {
            background: rgba(0,183,255,0.16);
            border: 1px solid rgba(0,183,255,0.8);
            box-shadow: 0 0 20px rgba(0,183,255,0.5);
            transform: scale(1.03);
        }

        .stRadio p {
            font-size: 20px !important;
            font-weight: 600 !important;
            text-shadow: 0 0 10px #00b7ff,
                         0 0 20px #00b7ff;
            transition: opacity 0.2s ease, transform 0.2s ease;
        }

        .stRadio label:hover p {
            transform: translateX(6px);
        }

        /* Hide radio circle */
        .stRadio input[type="radio"] {
            display: none !important;
        }

        /* Collapsed state text hiding */
        [data-testid="stSidebar"]:not(:hover) .stRadio p,
        [data-testid="stSidebar"]:not(:hover) .stRadio label {
            opacity: 0;
            visibility: hidden;
            width: 0px !important;
            padding: 0 !important;
            margin: 0 auto !important;
            border: none !important;
            background: transparent !important;
        }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        selection = st.radio(
            "Navigation",
            ["VISION  \nTERMINAL", "SYSTEM OBJECTIVES", 
             "ABOUT  \nAUTHOR"],
            label_visibility="collapsed"
        )

    return selection