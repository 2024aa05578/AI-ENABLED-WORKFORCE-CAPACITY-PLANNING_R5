import streamlit as st
import pandas as pd
from workforce_model import calculate_workforce

# --------------------------------------------------
# PAGE SETUP
# --------------------------------------------------

st.set_page_config(
    page_title="AI Enabled Workforce & Capacity Planning",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# BU-WISE PARAMETERS
# --------------------------------------------------

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
            key="ia_bau"
        ),
        "DC": st.slider(
            "Industrial Automation DC Surge %",
            0, 100, 5,
            key="ia_dc"
        ),
        "Attrition": st.slider(
            "Industrial Automation Attrition %",
            0, 30, 8,
            key="ia_attr"
        )
    }

# --------------------------------------------------
# MAIN PAGE
# --------------------------------------------------

st.title("🚀 AI Enabled Workforce & Capacity Planning")

st.markdown("""
### Service Workforce Forecasting

Workforce calculation is based on:

- Breakdown Maintenance Work Orders
- Preventive Maintenance Work Orders
- Startup & Commissioning Work Orders
- Business As Usual (BAU) Growth
- Data Center Surge Growth
- Attrition Impact
""")

uploaded_file = st.file_uploader(
    "Upload workforce_input.csv",
    type=["csv"]
)

# --------------------------------------------------
# PROCESS DATA
# --------------------------------------------------

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Input Data")

    st.dataframe(
        df,
        use_container_width=True
    )

    result = calculate_workforce(
        df,
        bu_parameters
    )

    st.subheader("📊 Workforce Planning Results")

    st.dataframe(
        result,
        use_container_width=True
    )

    # --------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------

    total_current = df["Current_SE"].sum()

    total_available = round(
        result["Available Engineers"].sum(),
        1
    )

    total_required = round(
        result["Required Engineers"].sum(),
        1
    )

    total_hiring = int(
        result["Additional Required"].sum()
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Current Engineers",
        total_current
    )

    c2.metric(
        "Available After Attrition",
        total_available
    )

    c3.metric(
        "Required Engineers",
        total_required
    )

    c4.metric(
        "Additional Hiring Required",
        total_hiring
    )

    # --------------------------------------------------
    # PRODUCT SUMMARY
    # --------------------------------------------------

    st.subheader("📦 Hiring Requirement by BU")

    product_summary = (
        result.groupby("Product")
        ["Additional Required"]
        .sum()
    )

    st.bar_chart(product_summary)

    # --------------------------------------------------
    # REGION SUMMARY
    # --------------------------------------------------

    st.subheader("🌍 Hiring Requirement by Region")

    region_summary = (
        result.groupby("Region")
        ["Additional Required"]
        .sum()
    )

    st.bar_chart(region_summary)

    # --------------------------------------------------
    # MATRIX
    # --------------------------------------------------

    st.subheader("📈 Product vs Region Hiring Matrix")

    pivot = result.pivot_table(
        values="Additional Required",
        index="Product",
        columns="Region",
        aggfunc="sum",
        fill_value=0
    )

    st.dataframe(
        pivot,
        use_container_width=True
    )

    # --------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------

    csv = result.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇ Download Results",
        data=csv,
        file_name="workforce_forecast.csv",
        mime="text/csv"
    )

else:

    st.info(
        "Upload workforce_input.csv to start analysis"
    )
