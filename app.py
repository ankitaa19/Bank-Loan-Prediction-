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

    st.subheader("🔍 Data Sent To Model")
    st.dataframe(model_input)

    prediction, probability = predictor.predict(model_input)

    st.divider()

    st.subheader("Prediction")

    if prediction == 1:

        confidence = probability[1]

        st.success("✅ Loan Approved")

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        st.progress(confidence)

        st.info(
            "The application satisfies the model's criteria for loan approval."
        )

    else:

        confidence = probability[0]

        st.error("❌ Loan Rejected")

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        st.progress(confidence)

        st.warning(
            "The application does not satisfy the model's approval criteria."
        )
