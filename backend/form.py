import streamlit as st


def loan_application_form():

    st.markdown(
        '<h2><i class="fa-solid fa-file-signature"></i> Loan Application Form</h2>',
        unsafe_allow_html=True
    )

    with st.form("loan_form"):

        st.markdown(
            '<h3><i class="fa-solid fa-user"></i> Personal Information</h3>',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=25
            )

            gender = st.selectbox(
                "Gender",
                ["Male", "Female"]
            )

            married = st.selectbox(
                "Married",
                ["Yes", "No"]
            )

        with col2:

            dependents = st.selectbox(
                "Dependents",
                [0, 1, 2, 3]
            )

            education = st.selectbox(
                "Education",
                ["Graduate", "Not Graduate"]
            )

            self_employed = st.selectbox(
                "Self Employed",
                ["Yes", "No"]
            )

        st.divider()

        st.markdown(
            '<h3><i class="fa-solid fa-wallet"></i> Financial Information</h3>',
            unsafe_allow_html=True
        )

        col3, col4 = st.columns(2)

        with col3:

            applicant_income = st.number_input(
                "Applicant Income",
                min_value=0
            )

            loan_amount = st.number_input(
                "Loan Amount",
                min_value=0
            )

        with col4:

            cibil_score = st.slider(
                "CIBIL Score",
                300,
                900,
                700
            )

            tenure = st.number_input(
                "Loan Tenure (Months)",
                min_value=1,
                value=12
            )

        st.divider()

        st.markdown(
            '<h3><i class="fa-solid fa-house"></i> Property Details</h3>',
            unsafe_allow_html=True
        )

        col5, col6 = st.columns(2)

        with col5:

            previous_loan = st.selectbox(
                "Previous Loan Taken",
                ["No", "Yes"]
            )

            property_area = st.selectbox(
                "Property Area",
                ["Urban", "Semiurban", "Rural"]
            )

        with col6:

            customer_bandwidth = st.selectbox(
                "Customer Bandwidth",
                ["Good", "Medium", "Bad"]
            )

        submit = col1, col2, col3 = st.columns([2, 2, 2])

        with col2:
            submit = st.form_submit_button(
                "Predict Loan",
                use_container_width=True
            )

    return submit, {
        "Age": age,
        "Dependents": dependents,
        "ApplicantIncome": applicant_income,
        "LoanAmount": loan_amount,
        "Cibil_Score": cibil_score,
        "Tenure": tenure,
        "Gender": gender,
        "Married": married,
        "Education": "Yes" if education == "Graduate" else "No",
        "Self_Employed": self_employed,
        "Previous_Loan_Taken": previous_loan,
        "Property_Area": property_area,
        "Customer_Bandwith": customer_bandwidth
    }
