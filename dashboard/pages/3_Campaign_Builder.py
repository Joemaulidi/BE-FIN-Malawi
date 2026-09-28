import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Campaign Builder | BE-FIN Malawi",
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

.stApp h1,
.stApp h2,
.stApp h3 {
    color: #0B1F3A !important;
    font-weight: 700 !important;
}

.stApp p,
.stApp label,
.stApp span {
    color: #111827;
}
.stApp div[data-testid="stMetric"] label,
.stApp div[data-testid="stMetric"] label *,
.stApp div[data-testid="stMetric"] [data-testid="stMetricLabel"],
.stApp div[data-testid="stMetric"] [data-testid="stMetricLabel"] * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

div[data-testid="stMetric"] {
    background-color: #0B1F3A !important;
    padding: 1.25rem !important;
    border-radius: 12px !important;
    border: 1px solid #0B1F3A !important;
    border-top: 3px solid #F28C28 !important;
    min-height: 110px !important;
}

div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] *,
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
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


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("Campaign Builder")

st.caption(
    "Behaviourally Informed Customer Campaigns"
)

st.markdown(
    """
    <div style="
        max-width: 850px;
        margin-top: 6px;
        margin-bottom: 10px;
        font-size: 14px;
        line-height: 1.7;
        color: #64748B;
    ">
        Translate behavioural insights into targeted customer campaigns,
        define interventions, and prepare campaigns for controlled testing.
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "Prototype • Synthetic Data • Behavioural Campaign Framework"
)

st.divider()


# --------------------------------------------------
# CAMPAIGN TARGETING
# --------------------------------------------------

st.subheader("Campaign Targeting")

target_col1, target_col2 = st.columns(2)
st.caption(
    "Define the customer group and intervention priority for this campaign."
)

with target_col1:
    campaign_segment = st.selectbox(
        "Select Behavioural Segment",
        customers["Behavioural_Segment"].unique()
    )

with target_col2:
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


campaign_count = len(campaign_customers)


if campaign_count == 0:

    st.warning(
        "No customers match the selected segment and intervention priority."
    )

    st.stop()


# --------------------------------------------------
# TARGET SUMMARY
# --------------------------------------------------

st.subheader("Campaign Target")
st.caption(
    "Overview of the customers reached by the selected campaign criteria."
)

target_col1, target_col2, target_col3 = st.columns(3)

with target_col1:
    st.metric(
        "Target Customers",
        f"{campaign_count:,}"
    )

with target_col2:
    campaign_percentage = (
        campaign_count / len(customers) * 100
    )

    st.metric(
        "Customer Base Reached",
        f"{campaign_percentage:.1f}%"
    )

with target_col3:
    st.metric(
        "Priority",
        campaign_priority
    )


# --------------------------------------------------
# RECOMMENDED INTERVENTION
# --------------------------------------------------

campaign_intervention = (
    campaign_customers["Recommended_Intervention"].mode()[0]
)

st.subheader("Recommended Intervention")
st.caption(
    "Behavioural action suggested for the selected customer segment."
)

st.info(
    campaign_intervention
)

st.caption(
    "Recommendation is based on the selected behavioural segment "
    "and intervention priority."
)


# --------------------------------------------------
# BEHAVIOURAL HYPOTHESIS
# --------------------------------------------------

if campaign_segment == "Consistent Saver":

    campaign_hypothesis = (
        "Reinforcing progress and existing routines may help customers "
        "maintain consistent saving behaviour."
    )

elif campaign_segment == "Irregular Saver":

    campaign_hypothesis = (
        "Planning or attention constraints may contribute to inconsistent "
        "saving, so timely reminders and small commitments may improve consistency."
    )

elif campaign_segment == "Low Savings Activity":

    campaign_hypothesis = (
        "Low salience of a savings goal or friction around saving may be "
        "limiting regular savings behaviour."
    )

elif campaign_segment == "Declining Engagement":

    campaign_hypothesis = (
        "Reduced attention or changing financial circumstances may be "
        "contributing to declining engagement."
    )

elif campaign_segment == "Dormant/Inactive":

    campaign_hypothesis = (
        "Reduced engagement or changing financial circumstances may be "
        "contributing to inactivity."
    )

else:

    campaign_hypothesis = (
        "Strengthening goal orientation may encourage more consistent "
        "financial behaviour."
    )


st.subheader("Behavioural Hypothesis")
st.caption(
    "The behavioural explanation guiding the proposed campaign intervention."
)
st.write(
    campaign_hypothesis
)

st.caption(
    "The behavioural hypothesis is a testable explanation, "
    "not a confirmed diagnosis."
)


# --------------------------------------------------
# CAMPAIGN OBJECTIVE
# --------------------------------------------------

if campaign_segment == "Consistent Saver":

    campaign_objective = (
        "Reinforce consistent saving behaviour and encourage continued "
        "progress toward savings goals."
    )

elif campaign_segment == "Irregular Saver":

    campaign_objective = (
        "Increase the consistency and frequency of customer saving behaviour."
    )

elif campaign_segment == "Low Savings Activity":

    campaign_objective = (
        "Encourage customers to establish a regular savings routine."
    )

elif campaign_segment == "Declining Engagement":

    campaign_objective = (
        "Re-engage customers and encourage renewed financial activity."
    )

elif campaign_segment == "Dormant/Inactive":

    campaign_objective = (
        "Encourage low-friction reactivation and renewed engagement "
        "with the financial service."
    )

else:

    campaign_objective = (
        "Strengthen goal-oriented financial behaviour and ongoing "
        "customer engagement."
    )


st.subheader("Campaign Objective")
st.caption(
    "Define the behavioural change the campaign is intended to encourage."
)
st.write(
    campaign_objective
)


# --------------------------------------------------
# CAMPAIGN MEASUREMENT
# --------------------------------------------------

st.subheader("Campaign Measurement")
st.caption(
    "Define the outcomes that will be used to assess campaign effectiveness."
)
st.write(
    "**Primary Outcome:** Change in savings deposits per month"
)

st.write(
    "**Secondary Outcomes:** Savings amount, transaction activity, "
    "digital activity and customer retention"
)

st.caption(
    "Outcomes should be measured against a control group where possible."
)


# --------------------------------------------------
# EXPERIMENT GROUP ALLOCATION
# --------------------------------------------------

st.subheader("Experiment Group Allocation")
st.caption(
    "Preview how the selected campaign audience is divided for controlled testing."
)

campaign_experiment = (
    campaign_customers["Experiment_Group"]
    .value_counts()
)

control_count = campaign_experiment.get("Control", 0)
treatment_count = campaign_experiment.get("Treatment", 0)

allocation_col1, allocation_col2 = st.columns(2)

with allocation_col1:

    st.metric(
        "Control Customers",
        f"{control_count:,}"
    )

with allocation_col2:

    st.metric(
        "Treatment Customers",
        f"{treatment_count:,}"
    )


if campaign_count > 0:

    control_percentage = (
        control_count / campaign_count * 100
    )

    treatment_percentage = (
        treatment_count / campaign_count * 100
    )

    st.caption(
        f"Allocation: {control_percentage:.1f}% Control | "
        f"{treatment_percentage:.1f}% Treatment"
    )


# --------------------------------------------------
# CAMPAIGN BRIEF
# --------------------------------------------------

st.subheader("Campaign Brief")

brief_col1, brief_col2, brief_col3 = st.columns(3)

with brief_col1:

    st.markdown("**TARGET SEGMENT**")
    st.write(campaign_segment)

with brief_col2:

    st.markdown("**PRIORITY**")
    st.write(campaign_priority)

with brief_col3:

    st.markdown("**TARGET CUSTOMERS**")
    st.write(f"{campaign_count:,}")


# --------------------------------------------------
# CAMPAIGN MESSAGE
# --------------------------------------------------

st.subheader("Campaign Message Preview")

campaign_channel = st.selectbox(
    "Select Communication Channel",
    ["SMS", "WhatsApp", "In-App Notification"]
)


if campaign_segment == "Consistent Saver":

    campaign_message = (
        "You're making good progress toward your savings goals. "
        "Keep your saving routine going and take another step toward your goal."
    )

elif campaign_segment == "Irregular Saver":

    campaign_message = (
        "Small, consistent savings can make a difference. "
        "Consider making your next savings contribution today."
    )

elif campaign_segment == "Low Savings Activity":

    campaign_message = (
        "Have a savings goal in mind? Start small and build the habit. "
        "Consider making your next savings contribution today."
    )

elif campaign_segment == "Declining Engagement":

    campaign_message = (
        "Your financial goals are still within reach. "
        "Take a moment today to review your savings and make your next contribution."
    )

elif campaign_segment == "Dormant/Inactive":

    campaign_message = (
        "Ready to get back on track? "
        "Consider making a small savings contribution and restart your financial routine."
    )

else:

    campaign_message = (
        "Take a moment to review your financial goals "
        "and consider your next savings contribution."
    )


channel_prefix = {
    "SMS": "",
    "WhatsApp": "Hi! 👋 ",
    "In-App Notification": "💡 "
}

campaign_message = (
    channel_prefix[campaign_channel]
    + campaign_message
)


st.info(
    campaign_message
)

st.caption(
    "Prototype message for behavioural testing. "
    "This message is not sent to customers."
)


# --------------------------------------------------
# CAMPAIGN STATUS
# --------------------------------------------------

st.divider()

st.subheader("Campaign Status")

st.info(
    "Draft — campaign has not been launched."
)


# --------------------------------------------------
# CREATE CAMPAIGN
# --------------------------------------------------

if st.button("Create Campaign"):

    st.success(
        f"Campaign created successfully for {campaign_count:,} customers."
    )

    st.write(
        "**Campaign Segment:**",
        campaign_segment
    )

    st.write(
        "**Priority:**",
        campaign_priority
    )

    st.write(
        "**Intervention:**",
        campaign_intervention
    )

    st.write(
        "**Primary Outcome:**",
        "Change in savings deposits per month"
    )