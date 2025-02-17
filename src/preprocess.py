import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def load_and_preprocess_data():
    """Load and preprocess the Iris dataset."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Split into train and test sets
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    
    # Save processed files
    train.to_csv("data/processed/train.csv", index=False)
    test.to_csv("data/processed/test.csv", index=False)

if __name__ == "__main__":
    load_and_preprocess_data()
