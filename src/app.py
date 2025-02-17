from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load trained model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Define request body schema
class InputData(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "ML Model is running!"}

@app.post("/predict/")
def predict(input_data: InputData):
    """Receive input features and return predictions."""
    features_array = np.array(input_data.features).reshape(1, -1)
    prediction = model.predict(features_array)
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
