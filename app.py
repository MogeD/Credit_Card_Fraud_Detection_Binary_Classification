from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler  # If you used scaling in your pipeline
from typing import List

# Load the trained model (adjust the file path to where your model is saved)
model = joblib.load("trained_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define the input data model using Pydantic
class PredictionInput(BaseModel):
    features: List[float]

# Define the /predict endpoint
@app.post("/predict")
async def predict(input_data: PredictionInput):
    # Extract features from the input
    features = np.array(input_data.features).reshape(1, -1)
    
    # scaler = joblib.load("scaler.pkl")  # Load scaler if applicable
    # features = scaler.transform(features)  # Scale features if needed

    # Make prediction using the trained model
    prediction = model.predict(features)

    # Return the prediction result
    return {"prediction": prediction[0]}

# Run the FastAPI app using Uvicorn
# If you're running from a script, use `uvicorn` to run the app:
# uvicorn app:app --reload
