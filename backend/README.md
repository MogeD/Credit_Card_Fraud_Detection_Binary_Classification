# Credit Card Fraud Detection API Backend

This is the backend service for the Credit Card Fraud Detection system. It provides a RESTful API for detecting fraudulent credit card transactions using machine learning.

## Directory Structure

```
backend/
├── app.py              # Main FastAPI application
├── requirements.txt    # Python dependencies
├── models/            # Directory for ML models
│   ├── trained_model.pkl
│   └── scaler.pkl
└── README.md          # This file
```

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure you have the following files in the `models` directory:

- `trained_model.pkl`: The trained machine learning model
- `scaler.pkl`: The feature scaler used during training

## Running the API

Start the FastAPI server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

### Endpoints

1. `GET /health`

   - Health check endpoint
   - Returns API status and timestamp

2. `POST /predict`
   - Predicts if a transaction is fraudulent
   - Input: Transaction features (time, amount, and PCA components)
   - Output: Prediction (0/1), probability, and timestamp

## Model Details

The model uses the following features:

- Time: Time elapsed since first transaction
- Amount: Transaction amount
- V1-V28: PCA transformed features for privacy protection

## Error Handling

The API includes comprehensive error handling for:

- Invalid input data
- Model loading failures
- Prediction errors
- Network issues

## Logging

Logs are written to the console with the following information:

- Timestamp
- Log level
- Module name
- Message
