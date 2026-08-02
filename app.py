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

    prediction, probability = predictor.predict(model_input)

    st.divider()

    st.subheader("Prediction")

    if prediction == 1:

        st.success("✅ Loan Approved")

        st.metric(
            "Confidence",
            f"{probability[1] * 100:.2f}%"
        )

        st.info(
            "The application satisfies the model's criteria for loan approval."
        )

    else:

        st.error("❌ Loan Rejected")

        st.metric(
            "Confidence",
            f"{probability[0] * 100:.2f}%"
        )

        st.warning(
            "The application does not satisfy the model's approval criteria."
        )
