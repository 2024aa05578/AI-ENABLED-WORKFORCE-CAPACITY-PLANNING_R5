import pandas as pd
import math

PRODUCTIVE_HOURS_PER_DAY = 7
WORKING_DAYS_PER_MONTH = 20
MONTHS_PER_YEAR = 12

FULL_CAPACITY = (
    PRODUCTIVE_HOURS_PER_DAY *
    WORKING_DAYS_PER_MONTH *
    MONTHS_PER_YEAR
)


def calculate_workforce(
    df,
    bu_parameters,
    target_utilization
):

    results = []

    effective_capacity = (
        FULL_CAPACITY *
        target_utilization / 100
    )

    for _, row in df.iterrows():

        product = row["Product"]

        params = bu_parameters.get(
            product,
            {
                "BAU": 20,
                "DC": 20,
                "Attrition": 8
            }
        )

        bau_growth = params["BAU"]
        dc_growth = params["DC"]
        attrition = params["Attrition"]

        current_hours = (
            row["Breakdown_WO"] * row["Breakdown_Hrs"]
            +
            row["PM_WO"] * row["PM_Hrs"]
            +
            row["Startup_WO"] * row["Startup_Hrs"]
        )

        future_hours = (
            current_hours *
            (
                1
                + bau_growth/100
                + dc_growth/100
            )
        )

        required_engineers = (
            future_hours /
            effective_capacity
        )

        available_engineers = (
            row["Current_SE"] *
            (
                1 -
                attrition/100
            )
        )

        additional_required = max(
            math.ceil(
                required_engineers -
                available_engineers
            ),
            0
        )

        results.append({

            "Region": row["Region"],
            "Product": row["Product"],

            "BAU Growth %": bau_growth,
            "DC Surge %": dc_growth,
            "Attrition %": attrition,
            "Utilization %": target_utilization,

            "Engineer Capacity":
                round(effective_capacity),

            "Current Hours":
                round(current_hours),

            "Future Hours":
                round(future_hours),

            "Required Engineers":
                round(required_engineers, 1),

            "Available Engineers":
                round(available_engineers, 1),

            "Additional Required":
                additional_required

        })

    return pd.DataFrame(results)
