import streamlit as st

def header_text(text, font_size="clamp(40px, 8vw, 90px)"):
    """
    Renders a futuristic, animated RGB signature title.
    :param text: The string to display
    :param font_size: CSS font-size (supports px, rem, or clamp)
    """
    st.markdown(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

        <style>
        /* Container cleanup */
        [data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {{
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
        }}

        .big-title {{
            font-family: 'Great Vibes', cursive !important;
            font-size: {font_size} !important; 
            line-height: 1.2;
            margin: 0;
            padding: 10px 0;
            text-align: center;
            white-space: nowrap; 
            
            /* Animated RGB Gradient Text */
            background: linear-gradient(to right, #ff0000, #00ff00, #00ffff, #ff00ff, #ff0000);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            
            /* Glow and Movement Animations */
            animation: 
                slideIn 1.5s ease-out,
                rainbow 4s linear infinite,
                glow-pulse 2s infinite alternate;
        }}

        @keyframes slideIn {{
            from {{opacity:0; transform:translateX(-50px);}}
            to   {{opacity:1; transform:translateX(0);}}
        }}

        @keyframes rainbow {{
            to {{ background-position: 200% center; }}
        }}

        @keyframes glow-pulse {{
            from {{ filter: drop-shadow(0 0 10px rgba(0, 198, 255, 0.4)); }}
            to {{ filter: drop-shadow(0 0 30px rgba(0, 114, 255, 0.8)); }}
        }}
        </style>

        <div class="big-title">{text}</div>
        """,
        unsafe_allow_html=True
    )



def draw_glowing_line():
    st.markdown(
        """
        <style>

        .glow-divider {
            height: 2px;
            width: 100%;
            margin-top: 10px;
            margin-bottom: 25px;

            background: linear-gradient(
                90deg,
                transparent,
                #00ffff,
                #8a2be2,
                #00ffff,
                transparent
            );

            background-size: 200% auto;

            border-radius: 999px;

            box-shadow:
                0 0 10px #00ffff,
                0 0 20px #8a2be2,
                0 0 40px rgba(138,43,226,0.8);

            animation: dividerFlow 4s linear infinite;
        }

        @keyframes dividerFlow {
            0% {
                background-position: 0% center;
            }

            100% {
                background-position: 200% center;
            }
        }

        </style>

        <div class="glow-divider"></div>
        """,
        unsafe_allow_html=True
    )



def subheader_text(text_input):
    """
    Renders a large, glowing, cursive subheader with a horizontal slide-in animation matching the header.
    """
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

    .subheading {{
        font-family: 'Great Vibes', cursive !important;
        font-size: 45px !important; 
        line-height: 1.2;
        margin: 10px 0;
        padding: 0;
        text-align: center; 
        color: #FFB6C1;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        
        /* Matching the animation behavior of the header_text function */
        animation: slideIn 1.5s ease-out forwards; 
    }}

    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateX(-50px); }}
        to   {{ opacity: 1; transform: translateX(0); }}
    }}
    </style>

    <div class="subheading">{text_input}</div>
    """, unsafe_allow_html=True)


def make_button_nice(font_style="elegant"):
    """
    Creates a styled button with multiple font options.
    
    Font options:
    - "cursive": Elegant Great Vibes (default)
    - "modern": Clean Orbitron for cyberpunk look
    - "bold": Impact/Bebas Neue for strong presence
    - "elegant": Playfair Display for sophisticated look
    """
    
    # Font configurations - INCREASED SIZES
    fonts = {
        "cursive": {
            "family": "'Great Vibes', cursive",
            "size": "68px",
            "weight": "normal",
            "spacing": "1px"
        },
        "modern": {
            "family": "'Orbitron', sans-serif",
            "size": "38px",
            "weight": "700",
            "spacing": "3px"
        },
        "bold": {
            "family": "'Bebas Neue', cursive",
            "size": "56px",
            "weight": "bold",
            "spacing": "2px"
        },
        "elegant": {
            "family": "'Playfair Display', serif",
            "size": "44px",
            "weight": "600",
            "spacing": "1.5px"
        }
    }
    
    font = fonts.get(font_style, fonts["cursive"])
    
    extra_import = ""
    if font_style == "bold":
        extra_import = "@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');"
    elif font_style == "elegant":
        extra_import = "@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&display=swap');"
    
    st.markdown(f"""
    <style>
    /* DOWNLOAD FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&display=swap');
    {extra_import}
    
    /* IMPROVE TEXT RENDERING FOR CLARITY */
    div[data-testid="stButton"] > button {{
        text-rendering: geometricPrecision !important;
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
    }}

    /* REMOVE EXTRA TOP/BOTTOM SPACE AND CENTER THE BUTTON CONTAINER */
    div[data-testid="stButton"] {{
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 15px auto !important;
        padding: 0px !important;
        width: 100% !important;
    }}

    /* REMOVE STREAMLIT BLOCK SPACING */
    div.element-container:has(div[data-testid="stButton"]) {{
        margin: 0rem !important;
        padding: 0rem !important;
    }}

    /* ACTUAL BUTTON - PREMIUM DESIGN WITH DARKER BACKGROUND */
    div[data-testid="stButton"] > button {{
        width: 320px !important;
        height: 120px !important;
        border-radius: 60px !important;
        
        /* Layout properties to enforce perfect internal content centering */
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        
        /* Darker gradient background - close to black */
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%) !important;
        
        /* BRIGHTER TEXT COLOR */
        color: #FFFFFF !important;
        text-shadow: 0 0 10px rgba(0,198,255,0.5), 0 0 20px rgba(0,114,255,0.3) !important;
        
        /* Glowing border */
        border: 2px solid rgba(0,198,255,0.5) !important;
        position: relative !important;
        overflow: hidden !important;
        
        /* FONT CONFIGURATION */
        font-family: {font['family']} !important;
        font-size: {font['size']} !important;
        font-weight: {font['weight']} !important;
        letter-spacing: {font['spacing']} !important;
        line-height: 1.2 !important;
        
        /* Shadows with glowing effect */
        box-shadow: 0 0 15px rgba(0,198,255,0.3),
                    0 0 30px rgba(0,114,255,0.2),
                    0 5px 15px rgba(0,0,0,0.3),
                    inset 0 1px 0 rgba(255,255,255,0.05) !important;
        
        /* Transitions */
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
        white-space: nowrap !important;
        padding: 0 20px !important;
    }}

    /* Enforce alignment and font parameters downstream onto raw text tags */
    div[data-testid="stButton"] > button *,
    div[data-testid="stButton"] > button span,
    div[data-testid="stButton"] > button p {{
        font-family: {font['family']} !important;
        text-align: center !important;
        display: inline-block !important;
        line-height: 1.2 !important;
    }}

    /* Pseudo-element for shine effect */
    div[data-testid="stButton"] > button::before {{
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: -100% !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(0,198,255,0.2), transparent) !important;
        transition: left 0.6s ease !important;
        pointer-events: none !important;
    }}

    /* Hover Effects */
    div[data-testid="stButton"] > button:hover {{
        transform: scale(1.05) translateY(-2px) !important;
        color: #ffffff !important;
        background: linear-gradient(135deg, #0f0f0f 0%, #1f1f1f 100%) !important;
        border-color: rgba(0,198,255,1) !important;
        text-shadow: 0 0 15px rgba(0,198,255,0.8), 0 0 30px rgba(0,114,255,0.5) !important;
        box-shadow: 0 0 25px #00c6ff,
                    0 0 50px rgba(0,114,255,0.5),
                    0 0 75px rgba(0,198,255,0.3),
                    0 10px 20px rgba(0,0,0,0.3) !important;
    }}

    /* Shine animation on hover */
    div[data-testid="stButton"] > button:hover::before {{
        left: 100% !important;
    }}

    /* Active/Click Effect */
    div[data-testid="stButton"] > button:active {{
        transform: scale(0.98) translateY(2px) !important;
        transition: all 0.1s ease !important;
    }}

    /* Focus ring (accessibility) with matching glow */
    div[data-testid="stButton"] > button:focus {{
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(0,198,255,0.4), 0 0 25px #00c6ff, 0 0 50px #0072ff !important;
        border-color: rgba(0,198,255,0.7) !important;
    }}
    </style>
    """, unsafe_allow_html=True)




def paragraph_header_text(text_input):
    """
    Renders a static aurora borealis themed subheader with multi-color glow effect.
    No animations or motions - completely static.
    """
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

    .subheading-aurora {{
        font-family: 'Great Vibes', cursive !important;
        font-size: 45px !important; 
        line-height: 1.2;
        margin: 10px 0;
        padding: 0;
        text-align: left; 
        color: #E0F7FA;
        text-shadow: 0 0 10px #00FF88, 0 0 20px #00BCD4, 0 0 30px #4CAF50;
    }}
    </style>

    <div class="subheading-aurora">{text_input}</div>
    """, unsafe_allow_html=True)


def normal_text(content: str):
    st.markdown(f"""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet">
    <style>
        .intro-text-container {{
            font-family: 'Dancing Script', cursive, serif !important;
            font-size: 32px !important;
            color: #FFFFFF !important;
            line-height: 1.6;
            margin: 30px 0px;
            
            /* High visibility against moving blobs */
            text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
            
            /* Entry Animation */
            opacity: 0;
            animation: slideIn 1.5s ease-out forwards;
        }}

        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .highlight-orange {{
            color: #F39C12 !important;
            font-weight: bold;
        }}
    </style>

    <div class="intro-text-container">
        {content}
    </div>
    """, unsafe_allow_html=True)





