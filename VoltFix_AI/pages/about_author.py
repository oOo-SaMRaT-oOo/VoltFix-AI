import streamlit as st
import base64
from pathlib import Path
from functions.styling_used import draw_glowing_line
from functions.page_layout import make_page_nice

def display_about_author():

    make_page_nice()
    def load_image_base64(path):
        base_path = Path(__file__).parent
        abs_path = (base_path / path).resolve()
        
        if not abs_path.exists():
            st.error(f"File not found! I am looking for it at: {abs_path}")
            return "" 

        with open(abs_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    

    st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.36/bundled/lenis.min.js"></script>
    <script>
    const lenis = new Lenis({ duration: 1.2, smooth: true });
    function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
    </script>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Great+Vibes&display=swap');
    
    .big-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 80px !important;
        line-height: 1;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        animation: slideIn 1.5s ease-out;
    }

    .animated-img {
        animation: imgFadeIn 1.5s ease-in-out forwards;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    }

    @keyframes slideIn {
        from {opacity:0; transform:translateX(-100px);}
        to {opacity:1; transform:translateX(0);}
    }

    @keyframes imgFadeIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0px); }
    }
    </style>
    <div class="big-title">Samrat Malla</div>
    """, unsafe_allow_html=True)

    draw_glowing_line()

    c1, c2 = st.columns([5, 3])

    with c2:
        st.write("<br><br>",unsafe_allow_html=True)
        img_base64 = load_image_base64("Image/Pic.png")
        
        if img_base64:
            st.html(f"""
    <style>
    .animated-img {{
        animation: fadeIn 1.5s ease-in-out forwards;
        border-radius: 20px;
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to   {{ opacity: 1; transform: translateY(0px); }}
    }}
    </style>

    <img src="data:image/png;base64,{img_base64}" class="animated-img" width="300">
    """)

        st.markdown(
    "<p class='title-anim' style='text-align:center; font-size:0.9em; color:gray;'>~ Its me Haha ... </p>",
    unsafe_allow_html=True
)   

    with c1:
        st.markdown("""
        <style>
        .intro-text {
            font-family: 'Monotype Corsiva', cursive;
            font-size: 28px;
            color: #ffffff;
            line-height: 1.3;
            margin: 50px 20px;
            opacity: 0;
            transform: translateX(-100px);
            animation: slideIn 1.8s ease-out forwards;
            text-shadow: 0 0 12px #F4D03F;
        }
        .highlight-name { color:#F39C12; font-weight: bold; }
        </style>
        <div class="intro-text">
            <br>~ Hi, I’m <span class="highlight-name">Samrat Malla</span>,<br>
            an Electrical Engineering student passionate about blending engineering with software.
            I love using Python, simulations, and data-driven tools to solve real-world problems.
            My goal is to become a <i>software-based electrical engineer</i> who builds impactful solutions.
        </div>
        """, unsafe_allow_html=True)

    
    draw_glowing_line()
    
