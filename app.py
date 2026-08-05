import streamlit as st

from backend.predictor import LoanPredictor
from backend.preprocessing import LoanPreprocessor
from backend.form import loan_application_form

st.set_page_config(
    page_title="Bank Loan Prediction",
    page_icon=":material/account_balance:",
    layout="wide"
)

st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
    .icon-title {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>


/* Center the form submit button */
div[data-testid="stForm"] div[data-testid="stHorizontalBlock"] {
    justify-content: center;
}

/* Style the Predict Loan button */
div[data-testid="stForm"] button[kind="secondaryFormSubmit"] {
    background: linear-gradient(90deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 12px !important;
    height: 55px !important;
    transition: all 0.3s ease;
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.25);
}

div[data-testid="stForm"] button[kind="secondaryFormSubmit"]:hover {
    background: linear-gradient(90deg, #1d4ed8, #1e40af) !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35);
    cursor: pointer;
}

</style>
""", unsafe_allow_html=True)

predictor = LoanPredictor()
preprocessor = LoanPreprocessor()

submit, user_data = loan_application_form()

if submit:

    model_input = preprocessor.transform(user_data)

    prediction, probability = predictor.predict(model_input)

    st.divider()

    st.markdown(
        '<h3><i class="fa-solid fa-magnifying-glass-chart"></i> Prediction</h3>',
        unsafe_allow_html=True
    )

    if prediction == 1:

        confidence = probability[1]

        st.success("Loan Approved")

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        st.progress(confidence)

        st.info(
            "Based on the information provided, the application predicts that the loan is likely to be approved."
        )

    else:

        confidence = probability[0]

        st.error("Loan Rejected")

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        st.progress(confidence)

        st.warning(
            "Based on the information provided, the application predicts that the loan is likely to be rejected."
        )

    st.caption(
        "The confidence score indicates how certain the machine learning model is about its prediction."
    )
