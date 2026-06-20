# ====================================================
# PRODUCTIVITY PARAMETERS
# ====================================================

st.sidebar.title("Workforce Productivity")

productive_hours = st.sidebar.slider(
    "Productive Hours per Day",
    min_value=4,
    max_value=10,
    value=7
)

working_days = st.sidebar.slider(
    "Working Days per Month",
    min_value=15,
    max_value=26,
    value=20
)

target_utilization = st.sidebar.slider(
    "Target Service Engineer Utilization %",
    min_value=60,
    max_value=100,
    value=90
)
