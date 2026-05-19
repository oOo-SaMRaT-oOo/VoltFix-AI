# py -m streamlit run web_app.py

import streamlit as st
import joblib
from functions.mat_to_df import convert_mat_to_dataframe
import numpy as np
from functions.sidebar import custom_sidebar
from pages.vision_terminal import vision_terminal_display
from pages.system_objectives import write_system_objectives
from pages.about_author import display_about_author


@st.cache_data
def load_essentials():
    data = convert_mat_to_dataframe("simulation_data_demo.mat") # DataFrame

    features = ["Va_rms", "Vb_rms", "Vc_rms",
                 "Ia_rms", "Ib_rms", "Ic_rms", 
                 "In_rms"]
    
    model = joblib.load("VoltFix_AI_Model.pkl")

    test_probablities = model.predict_proba(data[features])

    probablity_any_fault = (test_probablities[:,1] + test_probablities[:,2]
                                    + test_probablities[:,3] )
    
    test_prediction = model.predict(data[features])

    test_prediction[probablity_any_fault > 0.1] = (np.argmax(test_probablities[
        probablity_any_fault>0.1,1:],axis = 1) + 1)
    test_prediction[probablity_any_fault <=0.1] = 0
    data["AI_DECISION"] = test_prediction
    return data


data = load_essentials()


options = custom_sidebar()


if options == "VISION  \nTERMINAL" :
    vision_terminal_display(data)


if options == "SYSTEM OBJECTIVES":
    write_system_objectives()    

if options =="ABOUT  \nAUTHOR":
    display_about_author()