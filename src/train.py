import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model():
    """Train a simple RandomForest model and save it."""
    train_df = pd.read_csv("data/processed/train.csv")
    
    X_train = train_df.iloc[:, :-1]  # Features
    y_train = train_df.iloc[:, -1]   # Target
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model()
