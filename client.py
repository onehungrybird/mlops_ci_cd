import requests

def get_prediction(features):
    """
    Send a POST request to the FastAPI model server to get a prediction.
    
    Args:
        features (list): A list of numerical features for model inference.
    
    Returns:
        dict: The response containing the predicted class.
    """
    url = "http://localhost:8000/predict/"
    headers = {"Content-Type": "application/json"}
    data = {"features": features}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    sample_input = [5.1, 3.5, 1.4, 0.2]  # Example input for the model
    result = get_prediction(sample_input)
    print(result)
