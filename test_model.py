from backend.predictor import LoanPredictor
from backend.preprocessing import LoanPreprocessor

# Load model and preprocessor
predictor = LoanPredictor()
preprocessor = LoanPreprocessor()

# Same values you entered in the Streamlit app
user_data = {
    "Age": 30,
    "Dependents": 0,
    "ApplicantIncome": 90000,
    "LoanAmount": 180000,
    "Cibil_Score": 810,
    "Tenure": 36,
    "Gender": "Male",
    "Married": "Yes",
    "Education": "Yes",
    "Self_Employed": "No",
    "Previous_Loan_Taken": "No",
    "Property_Area": "Urban",
    "Customer_Bandwith": "Good"
}

print("=" * 60)
print("Original Input")
print("=" * 60)
print(user_data)

# Transform input
model_input = preprocessor.transform(user_data)

print("\n" + "=" * 60)
print("Encoded Input Sent to Model")
print("=" * 60)
print(model_input)

# Predict
prediction, probability = predictor.predict(model_input)

print("\n" + "=" * 60)
print("Prediction Result")
print("=" * 60)

if prediction == 1:
    print("✅ Loan Approved")
else:
    print("❌ Loan Rejected")

print(f"\nPrediction Value : {prediction}")
print(f"Probability      : {probability}")
