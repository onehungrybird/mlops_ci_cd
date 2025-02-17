import unittest
from src.predict import predict

class TestModelPrediction(unittest.TestCase):
    def test_prediction_output(self):
        """Test if the model makes a valid prediction for a sample input."""
        sample_input = [5.1, 3.5, 1.4, 0.2]
        prediction = predict(sample_input)
        self.assertIn(prediction, [0, 1, 2], "Invalid class prediction!")

if __name__ == "__main__":
    unittest.main()
