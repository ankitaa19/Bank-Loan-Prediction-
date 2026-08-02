import streamlit as st

st.set_page_config(
    page_title="Bank Loan Prediction",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Loan Prediction System")

st.write("Welcome to the Bank Loan Prediction application.")

st.header("Applicant Details")

col1, col2 = st.columns(2)

with col1:
    st.text_input("Applicant Name")
    st.number_input("Applicant Income", min_value=0)

with col2:
    st.text_input("Loan Purpose")
    st.number_input("Loan Amount", min_value=0)

if st.button("Predict"):
    st.success("Prediction will appear here.")
