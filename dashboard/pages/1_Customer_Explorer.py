import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Explorer | BE-FIN Malawi",
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
.stApp *,
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] *,
section[data-testid="stSidebar"] a,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] p {
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
}

[data-testid="stMarkdownContainer"] p {
    color: #111827 !important;
}

[data-testid="stMarkdownContainer"] strong {
    color: #111827 !important;
}

[data-testid="stSelectbox"] label {
    color: #111827 !important;
}

[data-testid="stSelectbox"] div {
    color: #111827 !important;
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
customer_id = st.selectbox(
    "Select Customer",
    customers["Customer_ID"]
)

selected_customer = customers[
    customers["Customer_ID"] == customer_id
].iloc[0]

st.title("Customer Explorer")

st.subheader("Customer Behavioural Profile")

profile_col1, profile_col2 = st.columns(2)

with profile_col1:

    st.markdown(
        "<h3 style='color:#0B1F3A;'>SAVINGS BEHAVIOUR</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='color:#111827;'><b>Savings deposits per month:</b> "
        f"{selected_customer['Savings_Deposits_per_Month']}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='color:#111827;'><b>Months saved in last 6 months:</b> "
        f"{selected_customer['Months_Saved_Last_6M']}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='color:#111827;'><b>Average monthly savings (MWK):</b> "
        f"{selected_customer['Average_Monthly_Savings_MWK']:,.0f}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='color:#111827;'><b>Average balance (MWK):</b> "
        f"{selected_customer['Average_Balance_MWK']:,.0f}</p>",
        unsafe_allow_html=True
    )

with profile_col2:

    st.markdown(
        "<h3 style='color:#0B1F3A;'>ENGAGEMENT BEHAVIOUR</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='color:#111827;'><b>Monthly transactions:</b> "
        f"{selected_customer['Monthly_Transactions']}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='color:#111827;'><b>Digital transactions:</b> "
        f"{selected_customer['Digital_Transactions']}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='color:#111827;'><b>Days since last transaction:</b> "
        f"{selected_customer['Days_Since_Last_Transaction']}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='color:#111827;'><b>Savings goal:</b> "
        f"{selected_customer['Savings_Goal']}</p>",
        unsafe_allow_html=True
    )
st.subheader("Recommended Behavioural Intervention")

intervention = selected_customer["Recommended_Intervention"]

st.markdown("### Recommended Action")

st.info(intervention)

st.caption(
    "Prototype recommendation based on the customer's behavioural segment "
    "and intervention priority."
)