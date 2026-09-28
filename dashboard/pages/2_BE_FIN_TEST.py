import streamlit as st
import pandas as pd
from scipy import stats

st.set_page_config(
    page_title="BE-FIN TEST | BE-FIN Malawi",
    page_icon="BEFIN LOGO (1).png",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

html,
body,
[class*="css"],
.stApp,
.stApp * {
    font-family: 'Montserrat', sans-serif !important;
}
.stApp h1 {
    color: #0B1F3A !important;
    font-weight: 700 !important;
}
.stApp {
    background-color: #ffffff !important;
}
section[data-testid="stSidebar"] {
    background: #0B1F3A !important;
}

section[data-testid="stSidebar"] > div {
    background: #0B1F3A !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] a {
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] a[aria-current="page"] {
    background-color: #F28C28 !important;
    color: #FFFFFF !important;
    border-radius: 8px;
}

section[data-testid="stSidebar"] a[aria-current="page"] * {
    color: #FFFFFF !important;
}
/* Experiment Group Cards */

div[data-testid="stMetric"] {
    background-color: #0B1F3A !important;
    padding: 1.25rem !important;
    border-radius: 12px !important;
    border: 1px solid #0B1F3A !important;
    border-top: 3px solid #F28C28 !important;
    box-shadow: none !important;
    min-height: 110px !important;
}

div[data-testid="stMetric"] label,
div[data-testid="stMetric"] label *,
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] * {
    color: #FFFFFF !important;
}

div[data-testid="stMetricValue"] {
    font-size: 1.8rem !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricLabel"] {
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.4px;
    text-transform: uppercase;
}
.stApp p,
.stApp label,
.stApp span,
.stApp div {
    color: #111827 !important;
}
div[data-testid="stDataFrame"] *,
div[data-testid="stTable"] * {
    font-family: 'Montserrat', sans-serif !important;
}
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] *,
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}
button[data-testid="stBaseButton-headerNoPadding"] span[data-testid="stIconMaterial"],
button[data-testid="stExpandSidebarButton"] span[data-testid="stIconMaterial"] {
    font-size: 0 !important;
}

button[data-testid="stBaseButton-headerNoPadding"] span[data-testid="stIconMaterial"]::after {
    content: "‹" !important;
    font-family: Arial, sans-serif !important;
    font-size: 28px !important;
    font-weight: 400 !important;
    color: #F28C28 !important;
}

button[data-testid="stExpandSidebarButton"] span[data-testid="stIconMaterial"]::after {
    content: "›" !important;
    font-family: Arial, sans-serif !important;
    font-size: 28px !important;
    font-weight: 400 !important;
    color: #F28C28 !important;
}
</style>
""", unsafe_allow_html=True)

customers = pd.read_csv(
    "data/BE_FIN_customers.csv"
)

st.title("BE-FIN TEST")

st.caption(
    "Behavioural Intervention Experimentation"
)

st.markdown(
    """
    <div style="
        max-width: 850px;
        margin-top: 6px;
        margin-bottom: 10px;
    ">
        <div style="
            font-size: 14px;
            line-height: 1.7;
            color: #64748B;
        ">
            Test behavioural interventions using controlled experiments,
            compare customer outcomes, and measure behavioural response.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "Prototype • Synthetic Data • Experimental Framework"
)

st.divider()

experiment_counts = (
    customers["Experiment_Group"]
    .value_counts()
)
st.subheader("Experiment Groups")
st.subheader("Experiment Groups")

group_col1, group_col2 = st.columns(2)

with group_col1:
    st.metric(
        "Control Group",
        f"{experiment_counts.get('Control', 0):,}"
    )

with group_col2:
    st.metric(
        "Treatment Group",
        f"{experiment_counts.get('Treatment', 0):,}"
    )

st.caption(
    "Customers were randomly assigned to either the control or treatment group."
)
st.subheader("Experiment Design")

design_col1, design_col2 = st.columns(2)

with design_col1:
    st.markdown(
        """
        <div style="
            background:#F8FAFC;
            border:1px solid #E2E8F0;
            border-top:3px solid #0B1F3A;
            border-radius:10px;
            padding:20px;
            min-height:125px;
        ">
            <div style="
                font-size:11px;
                font-weight:700;
                color:#F28C28;
                letter-spacing:0.5px;
                margin-bottom:8px;
            ">
                CONTROL
            </div>
            <div style="
                font-size:14px;
                font-weight:600;
                color:#0B1F3A;
                margin-bottom:6px;
            ">
                Normal customer experience
            </div>
            <div style="
                font-size:12px;
                line-height:1.5;
                color:#64748B;
            ">
                Customers continue with the standard customer experience.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with design_col2:
    st.markdown(
        """
        <div style="
            background:#F8FAFC;
            border:1px solid #E2E8F0;
            border-top:3px solid #F28C28;
            border-radius:10px;
            padding:20px;
            min-height:125px;
        ">
            <div style="
                font-size:11px;
                font-weight:700;
                color:#F28C28;
                letter-spacing:0.5px;
                margin-bottom:8px;
            ">
                TREATMENT
            </div>
            <div style="
                font-size:14px;
                font-weight:600;
                color:#0B1F3A;
                margin-bottom:6px;
            ">
                Behavioural intervention
            </div>
            <div style="
                font-size:12px;
                line-height:1.5;
                color:#64748B;
            ">
                Customers receive a targeted behavioural intervention.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

design_col3, design_col4 = st.columns(2)

with design_col3:
    st.markdown(
        """
        <div style="
            background:#F8FAFC;
            border:1px solid #E2E8F0;
            border-top:3px solid #0B1F3A;
            border-radius:10px;
            padding:20px;
            min-height:125px;
        ">
            <div style="
                font-size:11px;
                font-weight:700;
                color:#F28C28;
                letter-spacing:0.5px;
                margin-bottom:8px;
            ">
                PRIMARY OUTCOME
            </div>
            <div style="
                font-size:14px;
                font-weight:600;
                color:#0B1F3A;
                margin-bottom:6px;
            ">
                Consistent saving behaviour
            </div>
            <div style="
                font-size:12px;
                line-height:1.5;
                color:#64748B;
            ">
                Measures whether customers save more consistently over time.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with design_col4:
    st.markdown(
        """
        <div style="
            background:#F8FAFC;
            border:1px solid #E2E8F0;
            border-top:3px solid #0B1F3A;
            border-radius:10px;
            padding:20px;
            min-height:125px;
        ">
            <div style="
                font-size:11px;
                font-weight:700;
                color:#F28C28;
                letter-spacing:0.5px;
                margin-bottom:8px;
            ">
                SECONDARY OUTCOMES
            </div>
            <div style="
                font-size:14px;
                font-weight:600;
                color:#0B1F3A;
                margin-bottom:6px;
            ">
                Broader financial behaviour
            </div>
            <div style="
                font-size:12px;
                line-height:1.5;
                color:#64748B;
            ">
                Savings amount, frequency, account activity and retention.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.subheader("Control vs Treatment")

comparison = (
    customers.groupby("Experiment_Group")
    .agg(
        Average_BES=("BES", "mean"),
        Average_Monthly_Savings=("Average_Monthly_Savings_MWK", "mean"),
        Average_Savings_Frequency=("Savings_Deposits_per_Month", "mean"),
        Average_Transactions=("Monthly_Transactions", "mean")
    )
    .round(2)
)
st.markdown("### Group Comparison")

comparison_display = comparison.rename(
    columns={
        "Average_BES": "Average BES",
        "Average_Monthly_Savings": "Avg. Monthly Savings (MWK)",
        "Average_Savings_Frequency": "Avg. Savings Frequency",
        "Average_Transactions": "Avg. Transactions"
    }
)

st.dataframe(
    comparison_display,
    width="stretch"
)

st.caption(
    "Baseline comparison of engagement, savings and transaction behaviour "
    "across the synthetic control and treatment groups."
)
st.subheader("Baseline Balance Check")

balance = (
    customers.groupby("Experiment_Group")
    .agg(
        Average_Age=("Age", "mean"),
        Average_BES=("BES", "mean"),
        Average_Savings=("Average_Monthly_Savings_MWK", "mean"),
        Average_Transactions=("Monthly_Transactions", "mean"),
        Average_Savings_Frequency=("Savings_Deposits_per_Month", "mean")
    )
    .round(2)
)

st.markdown("### Pre-Intervention Group Balance")

balance_display = balance.rename(
    columns={
        "Average_Age": "Average Age",
        "Average_BES": "Average BES",
        "Average_Savings": "Avg. Monthly Savings (MWK)",
        "Average_Transactions": "Avg. Transactions",
        "Average_Savings_Frequency": "Avg. Savings Frequency"
    }
)

st.dataframe(
    balance_display,
    width="stretch"
)

st.caption(
    "Pre-intervention comparison used to assess whether the synthetic "
    "control and treatment groups are broadly comparable before testing."
)
st.subheader("Synthetic Post-Intervention Results")

outcome_comparison = (
    customers.groupby("Experiment_Group")
    .agg(
        Baseline_Savings_Frequency=("Savings_Deposits_per_Month", "mean"),
        Post_Savings_Frequency=("Post_Intervention_Savings_Frequency", "mean")
    )
    .round(2)
)
outcome_comparison["Change"] = (
    outcome_comparison["Post_Savings_Frequency"]
    - outcome_comparison["Baseline_Savings_Frequency"]
).round(2)

outcome_display = outcome_comparison.rename(
    columns={
        "Baseline_Savings_Frequency": "Baseline Frequency",
        "Post_Savings_Frequency": "Post-Intervention Frequency",
        "Change": "Change"
    }
)

st.dataframe(
    outcome_display,
    width="stretch"
)

st.caption(
    "Synthetic comparison of savings frequency before and after the "
    "behavioural intervention."
)

st.dataframe(
    outcome_comparison,
    width="stretch"
)

st.caption(
    "Illustrative synthetic results only. "
    "These figures are simulated for prototype demonstration "
    "and do not represent real customer behaviour."
)
st.subheader("Difference-in-Differences Analysis")

control_change = (
    outcome_comparison.loc["Control", "Change"]
)

treatment_change = (
    outcome_comparison.loc["Treatment", "Change"]
)

did_effect = (
    treatment_change - control_change
)

st.markdown("### Estimated Behavioural Effect")

st.metric(
    "Difference-in-Differences Effect",
    f"{did_effect:.2f}",
    help="Synthetic prototype estimate: treatment change minus control change."
)

st.write(
    "The Difference-in-Differences estimate compares the change in "
    "savings frequency for the treatment group with the corresponding "
    "change in the control group."
)

st.caption(
    "Illustrative synthetic estimate only. "
    "This is not evidence of a real-world causal effect."
)
st.subheader("95% Confidence Interval")

customers["Change_in_Savings_Frequency"] = (
    customers["Post_Intervention_Savings_Frequency"]
    - customers["Savings_Deposits_per_Month"]
)

control_change_values = customers.loc[
    customers["Experiment_Group"] == "Control",
    "Change_in_Savings_Frequency"
]

treatment_change_values = customers.loc[
    customers["Experiment_Group"] == "Treatment",
    "Change_in_Savings_Frequency"
]

control_change_mean = control_change_values.mean()
treatment_change_mean = treatment_change_values.mean()

did_effect_raw = (
    treatment_change_mean
    - control_change_mean
)

control_change_se = stats.sem(control_change_values)
treatment_change_se = stats.sem(treatment_change_values)

did_se = (
    control_change_se**2
    + treatment_change_se**2
) ** 0.5

did_confidence_interval = stats.t.interval(
    0.95,
    df=len(control_change_values) + len(treatment_change_values) - 2,
    loc=did_effect_raw,
    scale=did_se
)

st.markdown("### Uncertainty Around the Estimated Effect")

ci_col1, ci_col2 = st.columns(2)

with ci_col1:
    st.metric(
        "Lower Bound",
        f"{did_confidence_interval[0]:.2f}"
    )

with ci_col2:
    st.metric(
        "Upper Bound",
        f"{did_confidence_interval[1]:.2f}"
    )

st.caption(
    "Approximate 95% confidence interval based on the difference in "
    "mean changes between the synthetic treatment and control groups."
)

st.info(
    "The interval represents the range of values around the synthetic "
    "effect estimate under this prototype calculation."
)
st.subheader("Savings Behaviour: Control vs Treatment")

chart_data = outcome_comparison[
    ["Baseline_Savings_Frequency", "Post_Savings_Frequency"]
].rename(
    columns={
        "Baseline_Savings_Frequency": "Baseline",
        "Post_Savings_Frequency": "Post-Intervention"
    }
)

st.bar_chart(
    chart_data,
    width="stretch"
)

st.caption(
    "Synthetic illustrative comparison of savings frequency before "
    "and after the intervention across experiment groups."
)
st.subheader("Treatment Effects by Behavioural Segment")

segment_effects = (
    customers[customers["Experiment_Group"] == "Treatment"]
    .groupby("Behavioural_Segment")
    .agg(
        Customers=("Customer_ID", "count"),
        Baseline_Savings_Frequency=("Savings_Deposits_per_Month", "mean"),
        Post_Savings_Frequency=("Post_Intervention_Savings_Frequency", "mean")
    )
    .round(2)
)

segment_effects["Change"] = (
    segment_effects["Post_Savings_Frequency"]
    - segment_effects["Baseline_Savings_Frequency"]
).round(2)

segment_effects_display = segment_effects.rename(
    columns={
        "Customers": "Customers",
        "Baseline_Savings_Frequency": "Baseline Frequency",
        "Post_Savings_Frequency": "Post-Intervention Frequency",
        "Change": "Change"
    }
)

st.dataframe(
    segment_effects_display,
    width="stretch"
)

st.caption(
    "Synthetic illustrative results showing how savings frequency changed "
    "across behavioural segments within the treatment group."
)
st.subheader("Segment-Level Savings Response")

segment_chart = segment_effects[
    ["Baseline_Savings_Frequency", "Post_Savings_Frequency"]
].rename(
    columns={
        "Baseline_Savings_Frequency": "Baseline",
        "Post_Savings_Frequency": "Post-Intervention"
    }
)

st.bar_chart(
    segment_chart,
    width="stretch"
)

st.caption(
    "Synthetic illustrative comparison of baseline and post-intervention "
    "savings frequency across behavioural segments."
)
st.subheader("Intervention Performance Matrix")

intervention_performance = (
    customers
    .groupby(["Behavioural_Segment", "Recommended_Intervention"])
    .agg(
        Customers=("Customer_ID", "count"),
        Average_Baseline=("Savings_Deposits_per_Month", "mean"),
        Average_Post=("Post_Intervention_Savings_Frequency", "mean")
    )
    .round(2)
)

intervention_performance["Change"] = (
    intervention_performance["Average_Post"]
    - intervention_performance["Average_Baseline"]
).round(2)

intervention_performance_display = intervention_performance.rename(
    columns={
        "Customers": "Customers",
        "Average_Baseline": "Baseline Frequency",
        "Average_Post": "Post-Intervention Frequency",
        "Change": "Change"
    }
)

st.dataframe(
    intervention_performance_display,
    width="stretch"
)

st.caption(
    "Synthetic illustrative matrix linking behavioural segments, "
    "recommended interventions and simulated behavioural change."
)
st.subheader("Intervention Opportunities")

opportunity_summary = (
    customers
    .groupby(["Intervention_Priority", "Behavioural_Segment"])
    .agg(
        Customers=("Customer_ID", "count")
    )
    .reset_index()
)

opportunity_summary = opportunity_summary.sort_values(
    ["Intervention_Priority", "Customers"],
    ascending=[True, False]
)

opportunity_display = opportunity_summary.rename(
    columns={
        "Intervention_Priority": "Priority",
        "Behavioural_Segment": "Behavioural Segment",
        "Customers": "Customers"
    }
)

st.dataframe(
    opportunity_display,
    width="stretch"
)

st.caption(
    "Prototype opportunity view showing where behavioural interventions "
    "could be considered across customer segments."
)

st.info(
    "Priority levels are illustrative and should be validated before "
    "deployment with real customer data."
)