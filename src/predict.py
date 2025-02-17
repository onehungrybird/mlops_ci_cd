import pickle
import numpy as np

def predict(sample_input):
    """Predict the class of a given sample input."""
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)

    prediction = model.predict(np.array(sample_input).reshape(1, -1))
    return prediction[0]

if __name__ == "__main__":
    sample = [5.1, 3.5, 1.4, 0.2]  # Example input
    print(f"Predicted class: {predict(sample)}")
