import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

DATA_PATH = Path("data/Bank_Loan.csv")


class LoanPreprocessor:

    def __init__(self):
        # Load dataset
        self.df = pd.read_csv(DATA_PATH)

        # Store all LabelEncoders
        self.encoders = {}

        # Create encoders for all categorical columns
        self.fit_encoders()

    def fit_encoders(self):
        """
        Create one LabelEncoder for each categorical column
        and store it inside self.encoders.
        """

        categorical_cols = self.categorical_columns()

        for column in categorical_cols:

            if column not in ["Loan_Status", "Loan_ID"]:

                encoder = LabelEncoder()

                encoder.fit(self.df[column])

                self.encoders[column] = encoder

    def show_mapping(self, column_name):
        """
        Returns the mapping of original values to encoded values.
        """

        encoder = self.encoders[column_name]

        mapping = {}

        for index, value in enumerate(encoder.classes_):
            mapping[value] = index

        return mapping

    def encode_value(self, column_name, value):
        """
        Encode a single categorical value.
        """

        encoder = self.encoders[column_name]

        return int(encoder.transform([value])[0])

    def transform(self, user_data):
        """
        Convert the entire user input into
        a DataFrame ready for prediction.
        """

        transformed_data = user_data.copy()

        # Encode categorical columns
        for column in self.encoders:

            transformed_data[column] = self.encode_value(
                column,
                transformed_data[column]
            )

        # Arrange columns in the order expected by the model
        feature_order = [
            "Age",
            "Dependents",
            "ApplicantIncome",
            "LoanAmount",
            "Cibil_Score",
            "Tenure",
            "Gender",
            "Married",
            "Education",
            "Self_Employed",
            "Previous_Loan_Taken",
            "Property_Area",
            "Customer_Bandwith"
        ]

        df = pd.DataFrame([transformed_data])

        df = df[feature_order]

        return df

    def dataset_info(self):
        return self.df

    def feature_columns(self):
        return self.df.drop("Loan_Status", axis=1).columns.tolist()

    def categorical_columns(self):
        return self.df.select_dtypes(include="object").columns.tolist()

    def numerical_columns(self):
        return self.df.select_dtypes(exclude="object").columns.tolist()
