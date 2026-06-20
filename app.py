import streamlit as st
import pandas as pd
from workforce_model import calculate_workforce

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Enabled Workforce & Capacity Planning",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# BU PARAMETERS
# =====================================================

st.sidebar.title("BU Wise Planning Parameters")

bu_parameters = {}

# UPS
with st.sidebar.expander("UPS", expanded=True):

    bu_parameters["UPS"] = {
        "BAU": st.slider("UPS BAU Growth %", 0, 100, 25),
        "DC": st.slider("UPS Data Center Surge %", 0, 100, 40),
        "Attrition": st.slider("UPS Attrition %", 0, 30, 8)
    }

# Cooling
with st.sidebar.expander("Cooling"):

    bu_parameters["Cooling"] = {
        "BAU": st.slider("Cooling BAU Growth %", 0, 100, 20),
        "DC": st.slider("Cooling Data Center Surge %", 0, 100, 50),
        "Attrition": st.slider("Cooling Attrition %", 0, 30, 8)
    }

# Power Products
with st.sidebar.expander("Power Products"):

    bu_parameters["Power Products"] = {
        "BAU": st.slider("Power Products BAU Growth %", 0, 100, 15),
        "DC": st.slider("Power Products DC Surge %", 0, 100, 10),
        "Attrition": st.slider("Power Products Attrition %", 0, 30, 8)
    }

# Power System
with st.sidebar.expander("Power System"):

    bu_parameters["Power System"] = {
        "BAU": st.slider("Power System BAU Growth %", 0, 100, 18),
        "DC": st.slider("Power System DC Surge %", 0, 100, 20),
