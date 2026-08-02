# 🏦 Bank Loan Prediction System

An end-to-end Machine Learning application that predicts whether a customer's loan application is likely to be **Approved** or **Rejected** based on their financial profile and personal details. The project demonstrates the complete machine learning workflow—from data preprocessing and model training to deployment through a user-friendly web application.

The application enables users to enter customer details such as income, loan amount, CIBIL score, education, employment status, property area, and previous loan history. These inputs are preprocessed using the same pipeline that was used during model training, ensuring consistency between training and inference. The processed data is then passed to a trained Decision Tree model, which predicts the loan status along with the prediction confidence.

The project follows an end-to-end deployment approach by integrating machine learning with an interactive frontend, allowing users to make real-time predictions without requiring any technical knowledge. The application is containerized using Docker and deployed on Streamlit Community Cloud, making it portable, reproducible, and accessible online.

---

# 📌 Project Overview

This project was developed to simulate how banks and financial institutions can automate the initial loan approval process using Machine Learning. Instead of manually evaluating every application, the model analyzes multiple customer attributes and predicts whether a loan is likely to be approved based on historical patterns learned during training.

The project covers the complete machine learning lifecycle, including:

- Data Collection and Exploration
- Data Cleaning and Preprocessing
- Feature Engineering
- Categorical Data Encoding
- Model Training using Decision Tree Classifier
- Model Evaluation
- Model Serialization using Pickle
- Interactive Streamlit Application
- Docker Containerization
- Cloud Deployment

---

# 🚀 Features

- Predicts Loan Approval Status in Real-Time
- Interactive and Responsive User Interface
- Confidence Score for Every Prediction
- Automated Data Preprocessing Pipeline
- Consistent Feature Encoding
- Decision Tree Based Classification Model
- Docker Support for Containerized Deployment
- Cloud Deployment using Streamlit Community Cloud

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit + HTML + CSS |
| Backend | Python (`app.py`) |
| Machine Learning | Scikit-learn (Decision Tree Classifier) |
| Data Processing | Pandas, NumPy |
| Model Training | Jupyter Notebook |
| Model Storage | Pickle (`build.pkl`) |
| Containerization | Docker |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

# 📂 Project Structure

```text
Bank-Loan-Prediction/
│
├── backend/
│   ├── form.py
│   ├── predictor.py
│   └── preprocessing.py
│
├── models/
│   └── build.pkl
│
├── csv/
│   └── loan.csv
│
├── app.py
├── requirements.txt
├── Dockerfile
├── test_model.py
├── .dockerignore
└── README.md
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/ankitaa19/Bank-Loan-Prediction-.git
```

### Navigate to Project Directory

```bash
cd Bank-Loan-Prediction-
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

# 🐳 Docker

### Build Docker Image

```bash
docker build -t bank-loan-prediction .
```

### Run Docker Container

```bash
docker run -p 8501:8501 bank-loan-prediction
```

---

# 🧠 Machine Learning Workflow

The machine learning pipeline implemented in this project consists of the following stages:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Label Encoding
- Train-Test Split
- Decision Tree Model Training
- Model Evaluation
- Model Serialization using Pickle
- Real-Time Prediction Pipeline
- Application Deployment

---

# 📊 Input Features

The model predicts loan approval based on the following customer attributes:

- Age
- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Loan Amount
- CIBIL Score
- Loan Tenure
- Previous Loan Taken
- Property Area
- Customer Bandwidth

---

# 📈 Prediction Output

The application provides:

- Loan Approval Status (Approved / Rejected)
- Prediction Confidence Score

---

# 🌟 Key Highlights

- End-to-End Machine Learning Project
- Interactive Web Application
- Automated Prediction Pipeline
- Clean Modular Project Architecture
- Docker-Based Containerization
- Cloud Deployment
- Real-Time Loan Eligibility Prediction
- Consistent Data Preprocessing Pipeline
- Production-Ready Project Structure

---

# 👩‍💻 Author

**Ankita Lokhande**

- GitHub: https://github.com/ankitaa19
- LinkedIn: *(Add your LinkedIn Profile)*

---

## ⭐ If you found this project helpful, consider giving it a star!
