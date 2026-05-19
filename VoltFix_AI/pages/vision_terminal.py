import streamlit as st
from functions.styling_used import header_text,paragraph_header_text,subheader_text,draw_glowing_line,make_button_nice
from functions.page_layout import make_page_nice




def vision_terminal_display(data):

    make_page_nice()
    header_text("VoltFix : AI")
    st.markdown("<br>",unsafe_allow_html=True)
    sub_text = "~ Capture The Microsecond Chaos !"
    subheader_text(sub_text)
    draw_glowing_line()
    make_button_nice()

    if st.button(label = "Start Analysis"):
    

        st.write("---")
        paragraph_header_text("System Status :")
        st.markdown("<br>",unsafe_allow_html= True)
        trip_banner = st.empty()
        draw_glowing_line()


        paragraph_header_text("Phase Quantity Analysis :")
        col1,col2 = st.columns(2)
        V = col1.empty()
        I = col2.empty()
        draw_glowing_line()

        paragraph_header_text("Rms Quantity Analysis :")
        col1_rms,col2_rms = st.columns(2)
        V_rms = col1_rms.empty()
        I_rms = col2_rms.empty()



        draw_glowing_line()
        subheader_text("~ By Samrat Malla")



        refresh_rate = 1

        for index, row in data.iterrows():

            if index % refresh_rate != 0:
                continue

            window = data.iloc[max(0, index-400) : index+1]
            decision = int(row["AI_DECISION"])
            
            if decision == 0:
                trip_banner.success("🟢 SYSTEM STATUS: HEALTHY (NORMAL BALANCE)")
            elif decision == 1:
                trip_banner.error("🚨 BREAKER TRIPPED (AI RELAY) | FAULT TYPE: LINE-TO-GROUND (LG)")
            elif decision == 2:
                trip_banner.error("🚨 BREAKER TRIPPED (AI RELAY) | FAULT TYPE: LINE-TO-LINE (LL)")
            elif decision == 3:
                trip_banner.error("💥 SYSTEM EMERGENCY ISOLATION | FAULT TYPE: THREE-PHASE SYMMETRIC (LLL)")

            with V.container():
                st.subheader("VOLTAGE : ")
                st.line_chart(window[["Va", "Vb", "Vc"]], height=260)
                st.metric(label="PHASE A : PHASE VOLTAGE ( V )", value=f"{round(row['Va'],2)} V")
                st.metric(label="PHASE B : PHASE VOLTAGE ( V )", value=f"{round(row['Vb'],2)} V")
                st.metric(label="PHASE C : PHASE VOLTAGE ( V )", value=f"{round(row['Vc'],2)} V")
                
            with I.container():
                st.subheader("CURRENT :")
                st.line_chart(window[["Ia", "Ib", "Ic"]], height=260)
                st.metric(label="PHASE A : PHASE CURRENT ( Amp )", value=f"{round(row['Ia'],2)} A")
                st.metric(label="PHASE B : PHASE CURRENT ( Amp )", value=f"{round(row['Ib'],2)} A")
                st.metric(label="PHASE C : PHASE CURRENT ( Amp )", value=f"{round(row['Ic'],2)} A")
                
            with V_rms.container():
                st.subheader("VOLTAGE : ")
                st.line_chart(window[["Va_rms", "Vb_rms", "Vc_rms"]], height=260)
                st.metric(label="PHASE A : RMS VOLTAGE ( V )", value=f"{round(row['Va_rms'],2)} V")
                st.metric(label="PHASE B : RMS VOLTAGE ( V )", value=f"{round(row['Vb_rms'],2)} V")
                st.metric(label="PHASE C : RMS VOLTAGE ( V )", value=f"{round(row['Vc_rms'],2)} V")
                
            with I_rms.container():
                st.subheader("CURRENT : ")
                st.line_chart(window[["Ia_rms", "Ib_rms", "Ic_rms"]], height=260)
                st.metric(label="PHASE A : RMS CURRENT ( Amp )", value=f"{round(row['Ia_rms'],2)} A")
                st.metric(label="PHASE B : RMS CURRENT ( Amp )", value=f"{round(row['Ib_rms'],2)} A")
                st.metric(label="PHASE C : RMS CURRENT ( Amp )", value=f"{round(row['Ic_rms'],2)} A")
