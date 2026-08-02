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
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css\">
    <style>
    .icon-title {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .status-icon {
        margin-right: 0.35rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<h1 class="icon-title"><i class="fa-solid fa-building-columns"></i> Bank Loan Prediction</h1>',
    unsafe_allow_html=True
)

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
        st.markdown(
            '<p><i class="fa-solid fa-circle-check status-icon" style="color:#16a34a;"></i>Application approved based on model criteria.</p>',
            unsafe_allow_html=True
        )

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        st.progress(confidence)

        st.info("The application satisfies the model's criteria for loan approval.")
        st.markdown(
            '<p><i class="fa-solid fa-circle-info status-icon" style="color:#2563eb;"></i>Confidence shown above comes from model probability.</p>',
            unsafe_allow_html=True
        )

    else:

        confidence = probability[0]

        st.error("Loan Rejected")
        st.markdown(
            '<p><i class="fa-solid fa-circle-xmark status-icon" style="color:#dc2626;"></i>Application rejected based on model criteria.</p>',
            unsafe_allow_html=True
        )

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        st.progress(confidence)

        st.warning(
            "The application does not satisfy the model's approval criteria."
        )
        st.markdown(
            '<p><i class="fa-solid fa-triangle-exclamation status-icon" style="color:#d97706;"></i>Review applicant details before re-submission.</p>',
            unsafe_allow_html=True
        )
