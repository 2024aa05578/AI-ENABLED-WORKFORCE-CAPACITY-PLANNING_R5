# --------------------------------------------------
# UTILIZATION PARAMETER
# --------------------------------------------------

st.sidebar.title("Engineer Productivity")

target_utilization = st.sidebar.slider(
    "Target Service Engineer Utilization %",
    min_value=60,
    max_value=100,
    value=90,
    help="Planner utilization target considering leave, training, travel, meetings and work-life balance."
)
