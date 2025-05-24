# Credit Card Fraud Detection System

This project implements a machine learning-based system for detecting fraudulent credit card transactions. The system consists of a backend API service and a client application for testing.

## Project Structure

```
.
├── backend/           # Backend API service
│   ├── app.py        # FastAPI application
│   ├── models/       # ML models directory
│   │   ├── trained_model.pkl
│   │   └── scaler.pkl
│   ├── requirements.txt
│   └── README.md
├── client.py         # Test client application
├── data.csv          # Training data
├── oos_data.csv      # Out-of-sample test data
└── README.md         # This file
```

## Features

- Real-time fraud detection for credit card transactions
- RESTful API built with FastAPI
- Proper input validation and error handling
- Health check endpoint for monitoring
- Comprehensive logging
- Retry mechanism for failed requests
- Probability scores for predictions

## Setup

1. Set up the backend:

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

2. Start the backend server:

```bash
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

3. Test the system:

```bash
python client.py
```

## Documentation

- Backend API documentation: See `backend/README.md`
- API documentation (when server is running):
  - Interactive: `http://localhost:8000/docs`
  - Alternative: `http://localhost:8000/redoc`

## Model Details

The model uses the following features:

- Time: Time elapsed since first transaction
- Amount: Transaction amount
- V1-V28: PCA transformed features for privacy protection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
