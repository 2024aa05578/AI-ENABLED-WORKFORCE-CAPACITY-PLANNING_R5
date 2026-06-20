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
# SIDEBAR PARAMETERS
# =====================================================

st.sidebar.title("BU Wise Planning Parameters")

bu_parameters = {}

# UPS
with st.sidebar.expander("UPS", expanded=True):

    bu_parameters["UPS"] = {
        "BAU": st.slider(
            "UPS BAU Growth %",
            0, 100, 25,
            key="ups_bau"
        ),
        "DC": st.slider(
            "UPS Data Center Surge %",
            0, 100, 40,
            key="ups_dc"
        ),
        "Attrition": st.slider(
            "UPS Attrition %",
            0, 30, 8,
            key="ups_attr"
        )
    }

# Cooling
with st.sidebar.expander("Cooling"):

    bu_parameters["Cooling"] = {
        "BAU": st.slider(
            "Cooling BAU Growth %",
            0, 100, 20,
            key="cool_bau"
        ),
        "DC": st.slider(
            "Cooling Data Center Surge %",
            0, 100, 50,
            key="cool_dc"
        ),
        "Attrition": st.slider(
            "Cooling Attrition %",
            0, 30, 8,
            key="cool_attr"
        )
    }

# Power Products
with st.sidebar.expander("Power Products"):

    bu_parameters["Power Products"] = {
        "BAU": st.slider(
            "Power Products BAU Growth %",
            0, 100, 15,
            key="pp_bau"
        ),
        "DC": st.slider(
            "Power Products DC Surge %",
            0, 100, 10,
            key="pp_dc"
        ),
        "Attrition": st.slider(
            "Power Products Attrition %",
            0, 30, 8,
            key="pp_attr"
        )
    }

# Power System
with st.sidebar.expander("Power System"):

    bu_parameters["Power System"] = {
        "BAU": st.slider(
            "Power System BAU Growth %",
            0, 100, 18,
            key="ps_bau"
        ),
        "DC": st.slider(
            "Power System DC Surge %",
            0, 100, 20,
            key="ps_dc"
        ),
        "Attrition": st.slider(
            "Power System Attrition %",
            0, 30, 8,
            key="ps_attr"
        )
    }

# Industrial Automation
with st.sidebar.expander("Industrial Automation"):

    bu_parameters["Industrial Automation"] = {
        "BAU": st.slider(
            "Industrial Automation BAU Growth %",
            0, 100, 12,
