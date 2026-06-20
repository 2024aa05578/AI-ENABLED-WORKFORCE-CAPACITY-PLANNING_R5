import streamlit as st
import pandas as pd
from workforce_model import calculate_workforce

st.set_page_config(
    page_title="AI Enabled Workforce & Capacity Planning",
    page_icon="🚀",
    layout="wide"
)

# ====================================================
# SIDEBAR
# ====================================================

st.sidebar.title("BU Wise Planning Parameters")

bu_parameters = {}

# UPS
with st.sidebar.expander("UPS", expanded=True):

    bu_parameters["UPS"] = {
        "BAU": st.slider(
            "UPS BAU Growth %",
            0, 100, 25
        ),
        "DC": st.slider(
            "UPS Data Center Surge %",
            0, 100, 40
        ),
        "Attrition": st.slider(
            "UPS Attrition %",
            0, 30, 8
        )
    }

# Cooling
with st.sidebar.expander("Cooling"):

    bu_parameters["Cooling"] = {
        "BAU": st.slider(
            "Cooling BAU Growth %",
            0, 100, 20
        ),
        "DC": st.slider(
            "Cooling Data Center Surge %",
            0, 100, 50
        ),
        "Attrition": st.slider(
            "Cooling Attrition %",
            0, 30, 8
        )
    }

# Power Products
with st.sidebar.expander("Power Products"):

    bu_parameters["Power Products"] = {
        "BAU": st.slider(
            "Power Products BAU Growth %",
            0, 100, 15
        ),
        "DC": st.slider(
            "Power Products Data Center Surge %",
            0, 100, 10
        ),
        "Attrition": st.slider(
            "Power Products Attrition %",
            0, 30, 8
        )
    }

# Power System
with st.sidebar.expander("Power System"):

    bu_parameters["Power System"] = {
        "BAU": st.slider(
            "Power System BAU Growth %",
            0, 100, 18
        ),
        "DC": st.slider(
            "Power System Data Center Surge %",
            0, 100, 20
        ),
        "Attrition": st.slider(
            "Power System Attrition %",
            0, 30, 8
        )
    }

# Industrial Automation
with st.sidebar.expander("Industrial Automation"):

    bu_parameters["Industrial Automation"] = {
        "BAU": st.slider(
            "Industrial Automation BAU Growth %",
            0, 100, 12
        ),
        "DC": st.slider(
            "Industrial Automation Data Center Surge %",
            0, 100, 5
        ),
        "Attrition": st.slider(
            "Industrial Automation Attrition %",
            0, 30, 8
        )
    }

# ====================================================
# UTILIZATION
# ====================================================

st.sidebar.title("Engineer Productivity")

target_utilization = st.sidebar.slider(
    "Target Service Engineer Utilization %",
    min_value=60,
    max_value=100,
    value=90
)

# ====================================================
# MAIN SCREEN
# ====================================================

st.title("🚀 AI Enabled Workforce & Capacity Planning")

st.markdown("""
### Workforce Forecasting Model

This model predicts the future workforce requirement considering:

- Breakdown Maintenance Work Orders
- Preventive Maintenance Work Orders
- Startup & Commissioning Work Orders
- BAU Growth
- Data Center Growth
- Attrition
- Service Engineer Utilization
""")

uploaded_file = st.file_uploader(
    "Upload workforce_input.csv",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Input Data")

    st.dataframe(
        df,
        use_container_width=True
    )

    result = calculate_workforce(
        df,
        bu_parameters,
        target_utilization
    )

    st.subheader("Workforce Planning Results")

    st.dataframe(
        result,
        use_container_width=True
    )

    # KPI

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

    c1, c2, c3, c4, c5 = st.columns(5)

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
        "Hiring Gap",
        total_hiring
    )

    c5.metric(
        "Utilization %",
        target_utilization
    )

    # Product View

    st.subheader("📦 Hiring Requirement by BU")

    product_summary = (
        result.groupby("Product")
        ["Additional Required"]
        .sum()
    )

    st.bar_chart(product_summary)

    # Region View

    st.subheader("🌍 Hiring Requirement by Region")

    region_summary = (
        result.groupby("Region")
        ["Additional Required"]
        .sum()
    )

    st.bar_chart(region_summary)

    # Matrix

    st.subheader("📊 Product vs Region Hiring Matrix")

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

    # Download

    csv = result.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "⬇ Download Results",
        csv,
        "workforce_forecast.csv",
        "text/csv"
    )

else:

    st.info(
        "Upload workforce_input.csv to start analysis."
    )
