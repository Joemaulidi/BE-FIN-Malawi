import streamlit as st
import pandas as pd
from scipy import stats
# ---------------------------------------
# BE-FIN COMMAND CENTRE
# ---------------------------------------

st.set_page_config(
    page_title="BE-FIN Malawi",
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

/* Main page */
.stApp {
    background-color: #ffffff !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Headings */
.stApp h1 {
    color: #0B1F3A !important;
    font-size: 2.2rem;
    font-weight: 700 !important;
}

.stApp h2 {
    color: #0B1F3A !important;
    font-size: 1.5rem;
    font-weight: 700 !important;
    letter-spacing: -0.2px;
}

.stApp h3 {
    color: #0B1F3A !important;
    font-size: 1.15rem;
    font-weight: 600 !important;
}

.stApp [data-testid="stCaptionContainer"] {
    color: #64748B !important;
}

.stApp [data-testid="stCaptionContainer"] p {
    color: #64748B !important;
}

/* Sidebar */
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

/* Active sidebar page */
section[data-testid="stSidebar"] a[aria-current="page"] {
    background-color: #F28C28 !important;
    color: #FFFFFF !important;
    border-radius: 8px;
}

section[data-testid="stSidebar"] a[aria-current="page"] * {
    color: #FFFFFF !important;
}

/* KPI cards */
div[data-testid="stMetric"] {
    background-color: #0B1F3A !important;
    padding: 1.25rem !important;
    border-radius: 12px !important;
    border: 1px solid #0B1F3A !important;
    border-top: 3px solid #F28C28 !important;
    box-shadow: none !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(11, 31, 58, 0.12) !important;
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
    letter-spacing: -0.5px;
}

div[data-testid="stMetricLabel"] {
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.4px;
    text-transform: uppercase;
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
.decision-title {
    text-align: left !important;
    margin-left: 0 !important;
    padding-left: 0 !important;
    color: #0B1F3A !important;
    font-size: 24px !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;
}
</style>
""", unsafe_allow_html=True)
st.sidebar.title("BE-FIN Malawi")

st.sidebar.info(
    "Use the sections below to explore the BE-FIN prototype."
)
st.sidebar.markdown("### BE-FIN Modules")

st.sidebar.button("Command Centre")
st.sidebar.button("Customer Explorer")
st.sidebar.button("BE-FIN Test")
st.sidebar.button("Campaign Builder")
st.sidebar.divider()

st.sidebar.caption("BE-FIN Malawi")
st.sidebar.caption(
    "Behavioural Financial Inclusion Toolkit"
)

st.sidebar.caption(
    "Understand → Intervene → Measure"
)

st.sidebar.caption(
    "Prototype • Synthetic Data"
)

# Load customer data

customers = pd.read_csv(
    "data/BE_FIN_customers.csv"
)

# ---------------------------------------
# HEADER
# ---------------------------------------

st.title("BE-FIN Malawi")
st.caption("Behavioural Financial Intelligence Platform")
st.caption("Prototype • Synthetic Data")
st.subheader("Behavioural Financial Inclusion Command Centre")
st.success(
    "Prototype Status: Operational"
)

st.caption(
    "Synthetic demonstration environment • Behavioural analytics • "
    "Intervention testing"
)

st.write(
    "A prototype system for understanding customer behaviour, "
    "identifying engagement opportunities, and testing behavioural interventions."
)

st.divider()
st.header("Executive Snapshot")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customer Base",
    f"{len(customers):,}"
)

col2.metric(
    "Average Engagement",
    f"{customers['BES'].mean():.1f}"
)

col3.metric(
    "Intervention Opportunities",
    f"{customers['Intervention_Priority'].isin(['High', 'Very High']).sum():,}"
)

col4.metric(
    "Avg. Savings Frequency",
    f"{customers['Savings_Deposits_per_Month'].mean():.1f}"
)
st.subheader("BE-FIN Decision Cycle")

cycle = st.columns([1, 0.15, 1, 0.15, 1, 0.15, 1, 0.15, 1])

steps = [
    ("01", "DATA", "Customer signals"),
    ("02", "BEHAVIOUR", "Engagement patterns"),
    ("03", "DIAGNOSIS", "Behavioural hypotheses"),
    ("04", "INTERVENTION", "Targeted action"),
    ("05", "MEASUREMENT", "Test and learn")
]

for i, (number, title, description) in enumerate(steps):
    with cycle[i * 2]:
        st.markdown(
            f"""
            <div style="
                background:#F8FAFC;
                border:1px solid #E2E8F0;
                border-top:3px solid #0B1F3A;
                border-radius:10px;
                padding:18px 10px;
                text-align:center;
                min-height:105px;
            ">
                <div style="font-size:12px;font-weight:700;color:#F28C28;">
                    {number}
                </div>
                <div style="font-size:14px;font-weight:700;color:#0B1F3A;margin-top:6px;">
                    {title}
                </div>
                <div style="font-size:11px;color:#64748B;margin-top:5px;">
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if i < 4:
        with cycle[i * 2 + 1]:
            st.markdown(
                "<div style='text-align:center;padding-top:42px;color:#F28C28;font-size:20px;font-weight:600;'>→</div>",
                unsafe_allow_html=True
            )
st.write(
    "Understand customer behaviour → Identify behavioural opportunities "
    "→ Design interventions → Test → Measure outcomes"
)
col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "**UNDERSTAND**\n\n"
        "Analyse customer behaviour and identify engagement patterns."
    )

with col2:
    st.info(
        "**INTERVENE**\n\n"
        "Match behavioural opportunities with targeted interventions."
    )

with col3:
    st.info(
        "**MEASURE**\n\n"
        "Test interventions and measure changes in customer behaviour."
    )
    st.divider()

st.header("Customer Engagement Overview")

engagement_counts = (
    customers["Engagement_Band"]
    .value_counts()
    .reindex(
        ["Low", "Moderate", "High", "Very High"],
        fill_value=0
    )
)

col1, col2 = st.columns([2, 1])

with col1:
    st.bar_chart(engagement_counts)

with col2:
    st.markdown("### Engagement Distribution")

    st.metric(
        "Low Engagement",
        f"{engagement_counts['Low']:,}"
    )

    st.metric(
        "Moderate Engagement",
        f"{engagement_counts['Moderate']:,}"
    )

    st.metric(
        "High + Very High",
        f"{engagement_counts['High'] + engagement_counts['Very High']:,}"
    )

st.caption(
    "Synthetic illustrative distribution of customers by "
    "Behavioural Engagement Score band."
)
st.header("Experiment Overview")

experiment_summary = (
    customers.groupby("Experiment_Group")
    .agg(
        Customers=("Customer_ID", "count"),
        Baseline_Savings_Frequency=("Savings_Deposits_per_Month", "mean"),
        Post_Savings_Frequency=("Post_Intervention_Savings_Frequency", "mean")
    )
    .round(2)
)

experiment_summary["Change"] = (
    experiment_summary["Post_Savings_Frequency"]
    - experiment_summary["Baseline_Savings_Frequency"]
).round(2)

did_effect = (
    experiment_summary.loc["Treatment", "Change"]
    - experiment_summary.loc["Control", "Change"]
)

col1, col2 = st.columns([2, 1])

with col1:
    st.dataframe(
        experiment_summary,
        width="stretch"
    )

with col2:
    st.markdown("### Experiment Summary")

    st.metric(
        "Control Group",
        f"{experiment_summary.loc['Control', 'Customers']:,}"
    )

    st.metric(
        "Treatment Group",
        f"{experiment_summary.loc['Treatment', 'Customers']:,}"
    )

    st.metric(
        "DiD Effect",
        f"{did_effect:.2f}"
    )

st.caption(
    "Synthetic illustrative experiment results. "
    "These figures are simulated for prototype demonstration "
    "and do not represent real customer behaviour."
)

st.divider()

st.header("What BE-FIN Identifies")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="
            background:#F8FAFC;
            border:1px solid #E2E8F0;
            border-top:3px solid #F28C28;
            border-radius:10px;
            padding:20px;
            min-height:150px;
        ">
            <div style="
                font-size:12px;
                font-weight:700;
                color:#F28C28;
                margin-bottom:10px;
            ">
                01
            </div>
            <div style="
                font-size:14px;
                font-weight:700;
                color:#0B1F3A;
                margin-bottom:8px;
            ">
                BEHAVIOURAL PATTERNS
            </div>
            <div style="
                font-size:12px;
                line-height:1.6;
                color:#64748B;
            ">
                Identifies differences in customer saving and engagement behaviour.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="
            background:#F8FAFC;
            border:1px solid #E2E8F0;
            border-top:3px solid #F28C28;
            border-radius:10px;
            padding:20px;
            min-height:150px;
        ">
            <div style="
                font-size:12px;
                font-weight:700;
                color:#F28C28;
                margin-bottom:10px;
            ">
                02
            </div>
            <div style="
                font-size:14px;
                font-weight:700;
                color:#0B1F3A;
                margin-bottom:8px;
            ">
                INTERVENTION OPPORTUNITIES
            </div>
            <div style="
                font-size:12px;
                line-height:1.6;
                color:#64748B;
            ">
                Highlights customer groups where behavioural interventions can be tested.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style="
            background:#F8FAFC;
            border:1px solid #E2E8F0;
            border-top:3px solid #F28C28;
            border-radius:10px;
            padding:20px;
            min-height:150px;
        ">
            <div style="
                font-size:12px;
                font-weight:700;
                color:#F28C28;
                margin-bottom:10px;
            ">
                03
            </div>
            <div style="
                font-size:14px;
                font-weight:700;
                color:#0B1F3A;
                margin-bottom:8px;
            ">
                BEHAVIOURAL RESPONSE
            </div>
            <div style="
                font-size:12px;
                line-height:1.6;
                color:#64748B;
            ">
                Measures how customer behaviour changes following an intervention.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown(
    "<div class='decision-title'>Decision Intelligence</div>",
    unsafe_allow_html=True
)
st.caption("Translate behavioural evidence into a clear next action for the institution.")

st.divider()

st.divider()
st.subheader("Priority Opportunity")

priority_opportunity = (
    customers["Behavioural_Segment"]
    .value_counts()
    .idxmax()
)

priority_count = (
    customers["Behavioural_Segment"]
    .value_counts()
    .max()
)

st.info(
    f"**{priority_opportunity}** — the largest behavioural segment in "
    f"the current synthetic customer base, with **{priority_count:,} customers**."
)
st.subheader("Behavioural Interpretation")

if priority_opportunity == "Dormant/Inactive":
    observed_opportunity = (
        "A large group of customers shows no recent transaction activity, "
        "indicating an opportunity for customer re-engagement."
    )
    behavioural_hypothesis = (
        "Reduced engagement, account switching, or changing financial "
        "circumstances may contribute to inactivity."
    )

elif priority_opportunity == "Irregular Saver":
    observed_opportunity = (
        "A substantial group of customers saves intermittently rather than consistently."
    )
    behavioural_hypothesis = (
        "Planning or attention constraints may contribute to inconsistent saving."
    )

elif priority_opportunity == "Declining Engagement":
    observed_opportunity = (
        "Customer activity has declined, creating an opportunity for timely re-engagement."
    )
    behavioural_hypothesis = (
        "Reduced attention or changing financial circumstances may contribute to declining engagement."
    )

elif priority_opportunity == "Low Savings Activity":
    observed_opportunity = (
        "Customers remain relatively active but show limited savings activity."
    )
    behavioural_hypothesis = (
        "Low salience of a savings goal or friction around saving may contribute."
    )

elif priority_opportunity == "Consistent Saver":
    observed_opportunity = (
        "Customers demonstrate relatively consistent saving behaviour."
    )
    behavioural_hypothesis = (
        "Existing routines and goal-oriented behaviour may support continued saving."
    )

else:
    observed_opportunity = (
        "Customers remain generally active but do not fit a specific behavioural segment."
    )
    behavioural_hypothesis = (
        "There may be an opportunity to strengthen goal-oriented financial behaviour."
    )

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Observed Behaviour**")
    st.info(observed_opportunity)

with col2:
    st.markdown("**Behavioural Hypothesis**")
    st.info(behavioural_hypothesis)

st.caption(
    "Behavioural hypotheses are testable explanations, not confirmed diagnoses."
)

st.subheader("Recommended Institutional Action")

action_map = {
    "Dormant/Inactive": (
        "Launch a low-friction reactivation campaign focused on reminding "
        "customers of the value and convenience of using their existing account."
    ),
    "Irregular Saver": (
        "Introduce small-step savings commitments supported by timely reminders "
        "to encourage more consistent saving behaviour."
    ),
    "Declining Engagement": (
        "Deploy a timely re-engagement intervention using reminders and "
        "simple prompts to encourage renewed account activity."
    ),
    "Low Savings Activity": (
        "Introduce goal-setting prompts and reduce friction around making "
        "regular savings deposits."
    ),
    "Consistent Saver": (
        "Strengthen existing saving routines through progress feedback and "
        "goal reinforcement."
    ),
    "General Active": (
        "Use savings-goal prompts and progress feedback to strengthen "
        "goal-oriented financial behaviour."
    )
}

recommended_action = action_map.get(
    priority_opportunity,
    "Review the segment and identify an appropriate behavioural intervention."
)

st.markdown("**Recommended Action**")
st.success(recommended_action)

st.caption(
    "Prototype recommendation based on observed behavioural patterns and testable hypotheses."
)
st.subheader("Evidence & Decision Status")

evidence_col1, evidence_col2, evidence_col3 = st.columns(3)

with evidence_col1:
    st.metric(
        "Evidence Status",
        "Tested"
    )

with evidence_col2:
    st.metric(
        "Estimated Effect",
        f"{did_effect:.2f}",
        "savings deposits / month"
    )

with evidence_col3:
    control_changes = (
    customers.loc[
        customers["Experiment_Group"] == "Control",
        "Post_Intervention_Savings_Frequency"
    ]
    - customers.loc[
        customers["Experiment_Group"] == "Control",
        "Savings_Deposits_per_Month"
    ]
)

treatment_changes = (
    customers.loc[
        customers["Experiment_Group"] == "Treatment",
        "Post_Intervention_Savings_Frequency"
    ]
    - customers.loc[
        customers["Experiment_Group"] == "Treatment",
        "Savings_Deposits_per_Month"
    ]
)

control_se = stats.sem(control_changes)
treatment_se = stats.sem(treatment_changes)

did_se = (
    control_se**2
    + treatment_se**2
) ** 0.5

did_confidence_interval = stats.t.interval(
    0.95,
    df=len(control_changes) + len(treatment_changes) - 2,
    loc=did_effect,
    scale=did_se
)

st.metric(
    "95% Confidence Interval",
    f"{did_confidence_interval[0]:.2f} – {did_confidence_interval[1]:.2f}"
)
st.caption(
    "Synthetic experimental evidence. Results are illustrative and do not represent real bank customers."
)
st.subheader("Decision Pathway")

st.markdown(
    """
    <div style="color:#111827; line-height:1.7;">

    <strong>Current Evidence</strong>

    <p>The synthetic experiment indicates a positive change in savings frequency
    among customers receiving the behavioural intervention.</p>

    <p style="text-align:center; color:#F28C28; font-size:20px;">↓</p>

    <strong>Review Segment Response</strong>

    <p>Examine which behavioural segments showed the strongest response and
    whether the intervention appears suitable for those customer groups.</p>

    <p style="text-align:center; color:#F28C28; font-size:20px;">↓</p>

    <strong>Refine the Intervention</strong>

    <p>Adjust the intervention design based on observed segment-level response
    and behavioural hypotheses.</p>

    <p style="text-align:center; color:#F28C28; font-size:20px;">↓</p>

    <strong>Retest</strong>

    <p>Run another controlled experiment using real customer data before making
    broader deployment decisions.</p>

    </div>
    """,
    unsafe_allow_html=True
)

st.info(
    "**Current decision status:** Further testing and refinement recommended. "
    "The current results are synthetic and should not be treated as evidence "
    "for real-world deployment."
)
# ---------------------------------------
# KEY METRICS
# ---------------------------------------

total_customers = len(customers)
average_bes = customers["BES"].mean()
high_priority = (
    customers["Intervention_Priority"]
    .isin(["High", "Very High"])
    .sum()
)
segments = customers["Behavioural_Segment"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Average BES",
    f"{average_bes:.1f}"
)

col3.metric(
    "High / Very High Priority",
    f"{high_priority:,}"
)

col4.metric(
    "Behavioural Segments",
    segments
)

st.divider()

# ---------------------------------------
# BEHAVIOURAL SEGMENTS
# ---------------------------------------

st.header("Behavioural Segments")

segment_counts = (
    customers["Behavioural_Segment"]
    .value_counts()
)

st.bar_chart(segment_counts)

st.divider()

# ---------------------------------------
# CUSTOMER EXPLORER
# ---------------------------------------

st.header("Customer Explorer")

customer_id = st.selectbox(
    "Select Customer",
    customers["Customer_ID"]
)

selected_customer = customers[
    customers["Customer_ID"] == customer_id
].iloc[0]

st.caption(
    f"Customer ID: {selected_customer['Customer_ID']}"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Behavioural Engagement Score",
    f"{selected_customer['BES']:.1f}"
)

col2.metric(
    "Behavioural Segment",
    selected_customer["Behavioural_Segment"]
)

col3.metric(
    "Intervention Priority",
    selected_customer["Intervention_Priority"]
)
st.subheader("Customer Behavioural Profile")

profile_col1, profile_col2 = st.columns(2)

with profile_col1:
    st.markdown("**SAVINGS BEHAVIOUR**")

    st.write(
        "Savings deposits per month:",
        selected_customer["Savings_Deposits_per_Month"]
    )

    st.write(
        "Months saved in last 6 months:",
        selected_customer["Months_Saved_Last_6M"]
    )

    st.write(
        "Average monthly savings:",
        f"MWK {selected_customer['Average_Monthly_Savings_MWK']:,.0f}"
    )

    st.write(
        "Average balance:",
        f"MWK {selected_customer['Average_Balance_MWK']:,.0f}"
    )

with profile_col2:
    st.markdown("**ENGAGEMENT BEHAVIOUR**")

    st.write(
        "Monthly transactions:",
        selected_customer["Monthly_Transactions"]
    )

    st.write(
        "Digital transactions:",
        selected_customer["Digital_Transactions"]
    )

    st.write(
        "Days since last transaction:",
        selected_customer["Days_Since_Last_Transaction"]
    )

    st.write(
        "Savings goal:",
        selected_customer["Savings_Goal"]
    )


# ---------------------------------------
# BEHAVIOURAL DIAGNOSIS
# ---------------------------------------

st.subheader("Behavioural Diagnosis")

segment = selected_customer["Behavioural_Segment"]

if segment == "Consistent Saver":
    observed = "Customer saves consistently across multiple months."
    hypothesis = "Maintaining a clear savings routine may be supporting continued saving behaviour."

elif segment == "Irregular Saver":
    observed = "Customer saves intermittently rather than consistently."
    hypothesis = "Planning or attention constraints may contribute to inconsistent saving."

elif segment == "Low Savings Activity":
    observed = "Customer has low savings activity despite remaining relatively active."
    hypothesis = "Low salience of a savings goal or friction around saving may be contributing."

elif segment == "Declining Engagement":
    observed = "Customer activity has declined, with a relatively long period since the last transaction."
    hypothesis = "Reduced attention or changing financial circumstances may be contributing to declining engagement."

elif segment == "Dormant/Inactive":
    observed = "Customer has had no recent transaction activity."
    hypothesis = "Reduced engagement, account switching, or changing financial circumstances may explain inactivity."

else:
    observed = "Customer remains generally active but does not fit a specific behavioural segment."
    hypothesis = "There may be an opportunity to strengthen goal-oriented financial behaviour."

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Observed Behaviour")

    st.info(observed)

with col2:
    st.markdown("### Behavioural Hypothesis")

    st.info(hypothesis)

st.caption(
    "The behavioural hypothesis is a testable explanation, not a confirmed diagnosis."
)

# ---------------------------------------
# DATA PREVIEW
# ---------------------------------------

st.header("Customer Data")

st.caption(
    "Preview of the synthetic customer dataset used by the BE-FIN prototype."
)

data_col1, data_col2, data_col3 = st.columns(3)

with data_col1:
    st.metric(
        "Records",
        f"{len(customers):,}"
    )

with data_col2:
    st.metric(
        "Variables",
        f"{len(customers.columns):,}"
    )

with data_col3:
    st.metric(
        "Preview",
        "100 rows"
    )

st.dataframe(
    customers.head(100),
    width="stretch",
    height=420
)

st.caption(
    "Synthetic data for demonstration purposes only. "
    "It does not represent real bank customers."
)
# ---------------------------------------
# BE-FIN TEST
# ---------------------------------------

st.divider()

st.header("BE-FIN TEST")
st.write(
    "Prototype experimentation module for comparing "
    "customers receiving a behavioural intervention "
    "with customers receiving the normal customer experience."
)

experiment_counts = (
    customers["Experiment_Group"]
    .value_counts()
)

col1, col2 = st.columns(2)

col1.metric(
    "Control Group",
    f"{experiment_counts.get('Control', 0):,}"
)

col2.metric(
    "Treatment Group",
    f"{experiment_counts.get('Treatment', 0):,}"
)

st.subheader("Experiment Design")

st.write(
    "**Control:** Normal customer experience"
)

st.write(
    "**Treatment:** Behavioural intervention"
)

st.write(
    "**Primary outcome:** Consistent saving behaviour"
)

st.write(
    "**Secondary outcomes:** Savings amount, savings frequency, "
    "account activity and retention"
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

st.dataframe(
    comparison,
    use_container_width=True
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

st.dataframe(
    balance,
    use_container_width=True
)

st.caption(
    "Baseline balance is shown for prototype validation. "
    "The treatment and control groups were randomly assigned."
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

st.dataframe(
    outcome_comparison,
    width="stretch"
)

st.caption(
    "Illustrative synthetic results only. "
    "These figures are simulated for prototype demonstration "
    "and do not represent real customer behaviour."
)
st.subheader("Illustrative Treatment Effect")

control_change = outcome_comparison.loc[
    "Control", "Change"
]

treatment_change = outcome_comparison.loc[
    "Treatment", "Change"
]

illustrative_effect = (
    treatment_change - control_change
)
control_values = (
    customers.loc[
        customers["Experiment_Group"] == "Control",
        "Post_Intervention_Savings_Frequency"
    ]
)

treatment_values = (
    customers.loc[
        customers["Experiment_Group"] == "Treatment",
        "Post_Intervention_Savings_Frequency"
    ]
)

control_mean = control_values.mean()
treatment_mean = treatment_values.mean()

# ---------------------------------------
# DIFFERENCE-IN-DIFFERENCES CONFIDENCE INTERVAL
# ---------------------------------------

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

did_effect = (
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
    loc=did_effect,
    scale=did_se
)

st.metric(
    "Difference-in-Differences Effect",
    f"{illustrative_effect:.2f}",
    help="Synthetic prototype estimate: treatment change minus control change."
)
st.write(
    f"95% Confidence Interval: "
    f"{did_confidence_interval[0]:.2f} to "
    f"{did_confidence_interval[1]:.2f}"
)
st.caption(
    "Illustrative synthetic estimate only. "
    "This is not evidence of a real-world causal effect."
)
st.subheader("Experiment Interpretation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Experiment Result")

    st.metric(
        "Estimated Behavioural Effect",
        f"{illustrative_effect:.2f}",
        "savings deposits / month"
    )

    st.write(
        f"Based on the synthetic experiment, the treatment group "
        f"experienced a larger change in savings frequency than the "
        f"control group."
    )

with col2:
    st.markdown("### Statistical Range")

    st.metric(
        "95% Confidence Interval",
        f"{did_confidence_interval[0]:.2f} – "
        f"{did_confidence_interval[1]:.2f}"
    )

    st.write(
        f"Sample: {len(control_values):,} Control customers and "
        f"{len(treatment_values):,} Treatment customers."
    )

if did_confidence_interval[0] > 0:
    st.info(
        "In this synthetic prototype, the estimated effect remains above "
        "zero across the 95% confidence interval."
    )
else:
    st.info(
        "In this synthetic prototype, the 95% confidence interval includes zero."
    )

st.caption(
    "Prototype interpretation only. These results are simulated and "
    "should not be interpreted as evidence from real customers."
)
st.subheader("Savings Behaviour: Control vs Treatment")

chart_data = outcome_comparison[
    ["Baseline_Savings_Frequency", "Post_Savings_Frequency"]
]

st.bar_chart(chart_data)

st.caption(
    "Synthetic illustrative data showing baseline and post-intervention "
    "savings frequency by experiment group."
)
# ---------------------------------------
# TREATMENT EFFECTS BY SEGMENT
# ---------------------------------------

st.divider()

st.header("Treatment Effects by Behavioural Segment")

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

st.dataframe(
    segment_effects,
    width="stretch"
)

st.caption(
    "Synthetic illustrative results. Segment-level changes are simulated "
    "for prototype demonstration and do not represent real customer behaviour."
)
st.subheader("Segment-Level Savings Response")

segment_chart = segment_effects[
    ["Baseline_Savings_Frequency", "Post_Savings_Frequency"]
]

st.bar_chart(segment_chart)

st.caption(
    "Synthetic illustrative data showing baseline and post-intervention "
    "savings frequency among treatment customers by behavioural segment."
)
# ---------------------------------------
# INTERVENTION PERFORMANCE MATRIX
# ---------------------------------------

st.divider()

st.header("Intervention Performance Matrix")

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

st.dataframe(
    intervention_performance,
    width="stretch"
)

st.caption(
    "Synthetic illustrative results linking behavioural segments "
    "to recommended interventions and simulated behavioural change."
)
# ---------------------------------------
# INTERVENTION OPPORTUNITIES
# ---------------------------------------

st.divider()

st.header("Intervention Opportunities")

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

st.dataframe(
    opportunity_summary,
    width="stretch"
)

st.caption(
    "Prototype opportunity view based on synthetic customer data. "
    "Priority levels are illustrative and should be validated before "
    "use with real customers."
)
st.subheader("Customers by Intervention Priority")

priority_counts = (
    customers["Intervention_Priority"]
    .value_counts()
)

st.bar_chart(priority_counts)

st.caption(
    "Synthetic illustrative distribution of customers across "
    "intervention priority levels."
)
# ---------------------------------------
# CAMPAIGN BUILDER
# ---------------------------------------

st.divider()

st.header("Campaign Builder")

campaign_segment = st.selectbox(
    "Select Behavioural Segment",
    customers["Behavioural_Segment"].unique()
)

campaign_priority = st.selectbox(
    "Select Intervention Priority",
    ["All", "Very High", "High", "Medium", "Low"]
)

if campaign_priority == "All":
    campaign_customers = customers[
        customers["Behavioural_Segment"] == campaign_segment
    ]
else:
    campaign_customers = customers[
        (customers["Behavioural_Segment"] == campaign_segment)
        & (customers["Intervention_Priority"] == campaign_priority)
    ]

campaign_intervention = (
    campaign_customers["Recommended_Intervention"]
    .mode()[0]
)

campaign_count = len(campaign_customers)

col1, col2 = st.columns(2)

col1.metric(
    "Target Customers",
    f"{campaign_count:,}"
)

col2.write(
    "**Recommended Intervention**"
)

col2.info(
    campaign_intervention
)

st.caption(
    "Prototype campaign builder using synthetic customer data. "
    "Targeting logic should be validated before use with real customers."
)
st.subheader("Experiment Group Allocation")

campaign_experiment = (
    campaign_customers["Experiment_Group"]
    .value_counts()
)

col1, col2 = st.columns(2)

col1.metric(
    "Control Customers",
    f"{campaign_experiment.get('Control', 0):,}"
)

col2.metric(
    "Treatment Customers",
    f"{campaign_experiment.get('Treatment', 0):,}"
)
campaign_percentage = (
    campaign_count / len(customers) * 100
)

st.metric(
    "Share of Customer Base",
    f"{campaign_percentage:.1f}%"
)
st.subheader("Campaign Brief")

st.write("**Target Segment:**", campaign_segment)
st.write("**Intervention Priority:**", campaign_priority)
st.write("**Target Customers:**", f"{campaign_count:,}")
st.write("**Recommended Intervention:**", campaign_intervention)
if campaign_segment == "Consistent Saver":
    campaign_objective = "Reinforce consistent saving behaviour and encourage continued progress toward savings goals."

elif campaign_segment == "Irregular Saver":
    campaign_objective = "Increase the consistency and frequency of customer saving behaviour."

elif campaign_segment == "Low Savings Activity":
    campaign_objective = "Encourage customers to establish a regular savings routine."

elif campaign_segment == "Declining Engagement":
    campaign_objective = "Re-engage customers and encourage renewed financial activity."

elif campaign_segment == "Dormant/Inactive":
    campaign_objective = "Encourage low-friction reactivation and renewed engagement with the financial service."

else:
    campaign_objective = "Strengthen goal-oriented financial behaviour and ongoing customer engagement."

st.write("**Campaign Objective:**", campaign_objective)
if campaign_segment == "Consistent Saver":
    campaign_hypothesis = "Reinforcing progress and existing routines may help customers maintain consistent saving behaviour."

elif campaign_segment == "Irregular Saver":
    campaign_hypothesis = "Planning or attention constraints may contribute to inconsistent saving, so timely reminders and small commitments may improve consistency."

elif campaign_segment == "Low Savings Activity":
    campaign_hypothesis = "Low salience of a savings goal or friction around saving may be limiting regular savings behaviour."

elif campaign_segment == "Declining Engagement":
    campaign_hypothesis = "Reduced attention or changing financial circumstances may be contributing to declining engagement."

elif campaign_segment == "Dormant/Inactive":
    campaign_hypothesis = "Reduced engagement or changing financial circumstances may be contributing to inactivity."

else:
    campaign_hypothesis = "Strengthening goal orientation may encourage more consistent financial behaviour."

st.write("**Behavioural Hypothesis:**", campaign_hypothesis)

st.caption(
    "The behavioural hypothesis is a testable explanation, not a confirmed diagnosis."
)
st.write("**Primary Outcome:**", "Change in savings deposits per month")

st.write(
    "**Secondary Outcomes:**",
    "Savings amount, transaction activity, digital activity and customer retention"
)

st.caption(
    "Outcomes should be measured against a control group where possible."
)
if st.button("Create Campaign"):

    st.success(
        f"Campaign created successfully for {campaign_count:,} customers."
    )

    st.write("**Campaign Segment:**", campaign_segment)
    st.write("**Priority:**", campaign_priority)
    st.write("**Intervention:**", campaign_intervention)
    st.write("**Primary Outcome:**", "Change in savings deposits per month")