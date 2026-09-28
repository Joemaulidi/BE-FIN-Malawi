import pandas as pd
import numpy as np
np.random.seed(42)

n_customers = 10000
customer_ids = np.arange(1, n_customers + 1)

ages = np.random.randint(18, 66, n_customers)

sex = np.random.choice(
    ["Male", "Female"],
    size=n_customers
)

regions = np.random.choice(
    ["Central", "Northern", "Southern"],
    size=n_customers,
    p=[0.35, 0.20, 0.45]
)

urbanicity = np.random.choice(
    ["Urban", "Rural"],
    size=n_customers,
    p=[0.40, 0.60]
)
employment_status = np.random.choice(
    ["Employed", "Self-employed", "Student", "Unemployed"],
    size=n_customers,
    p=[0.35, 0.30, 0.15, 0.20]
)

income_frequency = np.random.choice(
    ["Daily", "Weekly", "Monthly", "Irregular"],
    size=n_customers,
    p=[0.15, 0.25, 0.40, 0.20]
)

income_band = np.random.choice(
    ["Below 100k", "100k-250k", "250k-500k", "Above 500k"],
    size=n_customers,
    p=[0.35, 0.30, 0.20, 0.15]
)
account_type = np.random.choice(
    ["Savings", "Current", "Mobile-linked"],
    size=n_customers,
    p=[0.50, 0.20, 0.30]
)

account_age_months = np.random.randint(
    1, 121, n_customers
)

monthly_transactions = np.random.poisson(
    lam=8,
    size=n_customers
)

digital_transactions = np.random.poisson(
    lam=4,
    size=n_customers
)

savings_deposits_per_month = np.random.poisson(
    lam=2,
    size=n_customers
)

months_saved_last_6m = np.random.randint(
    0, 7, n_customers
)
average_monthly_savings_mwk = np.random.lognormal(
    mean=8.5,
    sigma=1.0,
    size=n_customers
).round(0)

average_balance_mwk = np.random.lognormal(
    mean=9.5,
    sigma=1.1,
    size=n_customers
).round(0)

days_since_last_transaction = np.random.randint(
    0, 365,
    n_customers
)

income_receipts_month = np.random.poisson(
    lam=3,
    size=n_customers
)

savings_goal = np.random.choice(
    [
        "Emergency Fund",
        "School Fees",
        "Business",
        "Household Needs",
        "Asset Purchase",
        "No Specific Goal"
    ],
    size=n_customers,
    p=[0.20, 0.15, 0.15, 0.15, 0.10, 0.25]
)
customers = pd.DataFrame({
    "Customer_ID": customer_ids,
    "Age": ages,
    "Sex": sex,
    "Region": regions,
    "Urbanicity": urbanicity,
    "Employment_Status": employment_status,
    "Income_Frequency": income_frequency,
    "Income_Band": income_band,
    "Account_Type": account_type,
    "Account_Age_Months": account_age_months,
    "Monthly_Transactions": monthly_transactions,
    "Digital_Transactions": digital_transactions,
    "Savings_Deposits_per_Month": savings_deposits_per_month,
    "Months_Saved_Last_6M": months_saved_last_6m,
    "Average_Monthly_Savings_MWK": average_monthly_savings_mwk,
    "Average_Balance_MWK": average_balance_mwk,
    "Days_Since_Last_Transaction": days_since_last_transaction,
    "Income_Receipts_Month": income_receipts_month,
    "Savings_Goal": savings_goal
})
print(customers.head())
print("\nNumber of customers:", len(customers))
customers.to_csv(
    "data/BE_FIN_customers.csv",
    index=False
)

print("\nDataset saved successfully!")
# ---------------------------------------
# BE-FIN Behavioural Engagement Score
# ---------------------------------------

frequency_score = np.minimum(
    customers["Savings_Deposits_per_Month"] / 4 * 100,
    100
)

transaction_score = np.minimum(
    customers["Monthly_Transactions"] / 20 * 100,
    100
)

digital_score = np.minimum(
    customers["Digital_Transactions"] / 10 * 100,
    100
)

balance_score = np.minimum(
    customers["Average_Balance_MWK"] / 100000 * 100,
    100
)

recency_score = np.maximum(
    100 - (customers["Days_Since_Last_Transaction"] / 180 * 100),
    0
)

goal_score = np.where(
    customers["Savings_Goal"] == "No Specific Goal",
    40,
    100
)
customers["BES"] = (
    frequency_score * 0.25
    + transaction_score * 0.15
    + digital_score * 0.10
    + balance_score * 0.15
    + recency_score * 0.20
    + goal_score * 0.15
).round(1)
print("\nBES Summary:")
print(customers["BES"].describe())
customers["Engagement_Band"] = pd.cut(
    customers["BES"],
    bins=[0, 25, 50, 75, 100],
    labels=["Low", "Moderate", "High", "Very High"],
    include_lowest=True
)

print("\nEngagement Band Distribution:")
print(customers["Engagement_Band"].value_counts().sort_index())
conditions = [
    (
        (customers["Months_Saved_Last_6M"] >= 5) &
        (customers["BES"] >= 65)
    ),

    (
        (customers["Months_Saved_Last_6M"].between(2, 4)) &
        (customers["BES"] >= 45)
    ),

    (
        (customers["Savings_Deposits_per_Month"] <= 1) &
        (customers["BES"] < 50) &
        (customers["Days_Since_Last_Transaction"] <= 90)
    ),

    (
        (customers["Days_Since_Last_Transaction"] > 45) &
        (customers["Days_Since_Last_Transaction"] <= 120)
    ),

    (
        customers["Days_Since_Last_Transaction"] > 120
    )
]

segment_names = [
    "Consistent Saver",
    "Irregular Saver",
    "Low Savings Activity",
    "Declining Engagement",
    "Dormant/Inactive"
]

customers["Behavioural_Segment"] = np.select(
    conditions,
    segment_names,
    default="General Active"
)

print("\nBehavioural Segment Distribution:")
print(customers["Behavioural_Segment"].value_counts())
intervention_map = {
    "Consistent Saver":
        "Progress feedback + goal reinforcement",

    "Irregular Saver":
        "Small-step commitment + timely reminder",

    "Low Savings Activity":
        "Goal-setting + friction reduction",

    "Declining Engagement":
        "Re-engagement reminder + implementation intention",

    "Dormant/Inactive":
        "Low-friction reactivation message",

    "General Active":
        "Savings goal prompt + progress feedback"
}

customers["Recommended_Intervention"] = (
    customers["Behavioural_Segment"].map(intervention_map)
)

print("\nIntervention Recommendations:")
print(
    customers[
        [
            "Customer_ID",
            "Behavioural_Segment",
            "BES",
            "Recommended_Intervention"
        ]
    ].head(10)
)
customers.to_csv(
    "data/BE_FIN_customers.csv",
    index=False
)

print("\nBE-FIN dataset updated successfully!")
customers["Intervention_Priority"] = np.select(
    [
        customers["Days_Since_Last_Transaction"] > 270,
        customers["Days_Since_Last_Transaction"] > 180,
        customers["Days_Since_Last_Transaction"] > 120
    ],
    [
        "Very High",
        "High",
        "Medium"
    ],
    default="Low"
)

print("\nIntervention Priority:")
print(
    customers["Intervention_Priority"].value_counts()
)
customers.to_csv(
    "data/BE_FIN_customers.csv",
    index=False
)

print("\nBE-FIN dataset saved with intervention priority!")
# ---------------------------------------
# EXPERIMENT ASSIGNMENT
# ---------------------------------------

np.random.seed(123)

customers["Experiment_Group"] = np.random.choice(
    ["Control", "Treatment"],
    size=len(customers),
    p=[0.50, 0.50]
)
customers.to_csv(
    "data/BE_FIN_customers.csv",
    index=False
)

print("\nExperiment groups assigned successfully!")
# ---------------------------------------
# SYNTHETIC EXPERIMENT OUTCOMES
# ---------------------------------------

np.random.seed(456)

customers["Post_Intervention_Savings_Frequency"] = (
    customers["Savings_Deposits_per_Month"].astype(float)
)

treatment_effects = {
    "Consistent Saver": 0.15,
    "Irregular Saver": 0.55,
    "Low Savings Activity": 0.65,
    "Declining Engagement": 0.35,
    "Dormant/Inactive": 0.20,
    "General Active": 0.40
}

treatment_mask = customers["Experiment_Group"] == "Treatment"

customers.loc[treatment_mask, "Post_Intervention_Savings_Frequency"] += (
    customers.loc[treatment_mask, "Behavioural_Segment"]
    .map(treatment_effects)
    .fillna(0)
    .values
)

customers.loc[treatment_mask, "Post_Intervention_Savings_Frequency"] += (
    np.random.normal(
        loc=0,
        scale=0.25,
        size=treatment_mask.sum()
    )
)

customers["Post_Intervention_Savings_Frequency"] = (
    customers["Post_Intervention_Savings_Frequency"]
    .clip(lower=0)
    .round(2)
)

customers.to_csv(
    "data/BE_FIN_customers.csv",
    index=False
)

print("\nSynthetic experiment outcomes generated successfully!")