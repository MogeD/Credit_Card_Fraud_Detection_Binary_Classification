from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import List
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the trained model and scaler
try:
    model_path = os.path.join(current_dir, "trained_model.pkl")
    scaler_path = os.path.join(current_dir, "scaler.pkl")
    
    logger.info(f"Loading model from: {model_path}")
    logger.info(f"Loading scaler from: {scaler_path}")
    
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
    logger.info("Model and scaler loaded successfully")
except Exception as e:
    logger.error(f"Error loading model or scaler: {str(e)}")
    raise

# Initialize FastAPI app
app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="API for detecting fraudulent credit card transactions",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransactionFeatures(BaseModel):
    time: float = Field(..., description="Time elapsed since first transaction")
    amount: float = Field(..., description="Transaction amount")
    v1: float = Field(..., description="PCA transformed feature 1")
    v2: float = Field(..., description="PCA transformed feature 2")
    v3: float = Field(..., description="PCA transformed feature 3")
    v4: float = Field(..., description="PCA transformed feature 4")
    v5: float = Field(..., description="PCA transformed feature 5")
    v6: float = Field(..., description="PCA transformed feature 6")
    v7: float = Field(..., description="PCA transformed feature 7")
    v8: float = Field(..., description="PCA transformed feature 8")
    v9: float = Field(..., description="PCA transformed feature 9")
    v10: float = Field(..., description="PCA transformed feature 10")
    v11: float = Field(..., description="PCA transformed feature 11")
    v12: float = Field(..., description="PCA transformed feature 12")
    v13: float = Field(..., description="PCA transformed feature 13")
    v14: float = Field(..., description="PCA transformed feature 14")
    v15: float = Field(..., description="PCA transformed feature 15")
    v16: float = Field(..., description="PCA transformed feature 16")
    v17: float = Field(..., description="PCA transformed feature 17")
    v18: float = Field(..., description="PCA transformed feature 18")
    v19: float = Field(..., description="PCA transformed feature 19")
    v20: float = Field(..., description="PCA transformed feature 20")
    v21: float = Field(..., description="PCA transformed feature 21")
    v22: float = Field(..., description="PCA transformed feature 22")
    v23: float = Field(..., description="PCA transformed feature 23")
    v24: float = Field(..., description="PCA transformed feature 24")
    v25: float = Field(..., description="PCA transformed feature 25")
    v26: float = Field(..., description="PCA transformed feature 26")
    v27: float = Field(..., description="PCA transformed feature 27")
    v28: float = Field(..., description="PCA transformed feature 28")

class PredictionResponse(BaseModel):
    prediction: int = Field(..., description="0 for legitimate, 1 for fraudulent")
    probability: float = Field(..., description="Probability of fraud")
    timestamp: str = Field(..., description="Prediction timestamp")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/predict", response_model=PredictionResponse)
async def predict(transaction: TransactionFeatures):
    """
    Predict if a credit card transaction is fraudulent
    
    Args:
        transaction: Transaction features including time, amount, and PCA components
        
    Returns:
        PredictionResponse: Contains prediction (0/1), probability, and timestamp
    """
    try:
        # Convert input to numpy array
        features = np.array([[
            transaction.time, transaction.amount,
            transaction.v1, transaction.v2, transaction.v3, transaction.v4,
            transaction.v5, transaction.v6, transaction.v7, transaction.v8,
            transaction.v9, transaction.v10, transaction.v11, transaction.v12,
            transaction.v13, transaction.v14, transaction.v15, transaction.v16,
            transaction.v17, transaction.v18, transaction.v19, transaction.v20,
            transaction.v21, transaction.v22, transaction.v23, transaction.v24,
            transaction.v25, transaction.v26, transaction.v27, transaction.v28
        ]])
        
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0][1]
        
        logger.info(f"Prediction made: {prediction} with probability {probability:.4f}")
        
        return PredictionResponse(
            prediction=int(prediction),
            probability=float(probability),
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Error making prediction: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 