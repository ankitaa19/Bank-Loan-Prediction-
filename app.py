import streamlit as st

from backend.predictor import LoanPredictor
from backend.preprocessing import LoanPreprocessor
from backend.form import loan_application_form

st.set_page_config(
    page_title="Bank Loan Prediction",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Loan Prediction")

predictor = LoanPredictor()
preprocessor = LoanPreprocessor()


st.success("Model Loaded Successfully")

submit, user_data = loan_application_form()

if submit:

    st.success("Form Submitted Successfully!")

    model_input = preprocessor.transform(user_data)

    st.write("### Data Sent To Model")
    st.dataframe(model_input)
