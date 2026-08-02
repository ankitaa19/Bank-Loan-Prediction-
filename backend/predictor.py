import pickle
from pathlib import Path

MODEL_PATH = Path("models/build.pkl")


class LoanPredictor:
    def __init__(self):
        with open(MODEL_PATH, "rb") as file:
            self.model = pickle.load(file)

    def predict(self, data):
        prediction = self.model.predict(data)

        if hasattr(self.model, "predict_proba"):
            probability = self.model.predict_proba(data)
            return prediction[0], probability[0]

        return prediction[0], None
