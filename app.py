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
# SIDEBAR - BU PARAMETERS
# =====================================================

st.sidebar.title("BU Wise Planning Parameters")

bu_parameters = {}

# UPS
with st.sidebar.expander("UPS", expanded=True):

    ups_bau = st.slider("UPS BAU Growth %", 0, 100, 25)
    ups_dc = st.slider("UPS Data Center Surge %", 0, 100, 40)
    ups_attr = st.slider("UPS Attrition %", 0, 30, 8)

    bu_parameters["UPS"] = {
        "BAU": ups_bau,
        "DC": ups_dc,
        "Attrition": ups_attr
    }

# Cooling
with st.sidebar.expander("Cooling"):

    cooling_bau = st.slider("Cooling BAU Growth %", 0, 100, 20)
    cooling_dc = st.slider("Cooling Data Center Surge %", 0, 100, 50)
    cooling_attr = st.slider("Cooling Attrition %", 0, 30, 8)

    bu_parameters["Cooling"] = {
        "BAU": cooling_bau,
        "DC": cooling_dc,
        "Attrition": cooling_attr
    }

# Power Products
with st.sidebar.expander("Power Products"):

    pp_bau = st.slider("Power Products BAU Growth %", 0, 100, 15)
    pp_dc = st.slider("Power Products Data Center Surge %", 0, 100, 10)
    pp_attr = st.slider("Power Products Attrition %", 0, 30, 8)

    bu_parameters["Power Products"] = {
        "BAU": pp_bau,
        "DC": pp_dc,
        "Attrition": pp_attr
    }

# Power System
with st.sidebar.expander("Power System"):

