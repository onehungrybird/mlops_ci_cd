import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

def evaluate_model():
    """Evaluate the trained model on test data."""
    test_df = pd.read_csv("data/processed/test.csv")

    X_test = test_df.iloc[:, :-1]
    y_test = test_df.iloc[:, -1]

    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"Test Accuracy: {acc:.2f}")
    return acc

if __name__ == "__main__":
    evaluate_model()
