import unittest
import pandas as pd
import pickle
from src.train import train_model

class TestModelTraining(unittest.TestCase):
    def test_training_output(self):
        """Test if the training script successfully creates a model file."""
        train_model()
        try:
            with open("models/model.pkl", "rb") as f:
                model = pickle.load(f)
        except FileNotFoundError:
            self.fail("Model file not found. Training may have failed.")

    def test_model_accuracy(self):
        """Test if the trained model achieves reasonable accuracy."""
        from src.evaluate import evaluate_model

        acc = evaluate_model()  # Assuming evaluate_model() returns accuracy
        self.assertGreater(acc, 0.7, "Accuracy is too low!")

if __name__ == "__main__":
    unittest.main()
