import pandas as pd
import requests
import json
import logging
from typing import Dict, Any
from datetime import datetime
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FraudDetectionClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        
    def check_health(self) -> bool:
        """Check if the API is healthy"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Health check failed: {str(e)}")
            return False
            
    def predict_transaction(self, transaction_data: Dict[str, float], max_retries: int = 3) -> Dict[str, Any]:
        """
        Predict if a transaction is fraudulent
        
        Args:
            transaction_data: Dictionary containing transaction features
            max_retries: Maximum number of retry attempts
            
        Returns:
            Dictionary containing prediction results
        """
        for attempt in range(max_retries):
            try:
                response = self.session.post(
                    f"{self.base_url}/predict",
                    json=transaction_data,
                    timeout=5
                )
                response.raise_for_status()
                return response.json()
                
            except requests.exceptions.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    raise
                time.sleep(1)  # Wait before retrying

def main():
    # Initialize client
    client = FraudDetectionClient()
    
    # Check API health
    if not client.check_health():
        logger.error("API is not healthy. Exiting...")
        return
        
    # Load test data
    try:
        test_data = pd.read_csv('oos_data.csv')
        logger.info(f"Loaded {len(test_data)} test transactions")
    except Exception as e:
        logger.error(f"Error loading test data: {str(e)}")
        return
        
    # Process each transaction
    for idx, row in test_data.iterrows():
        try:
            # Convert row to dictionary
            transaction = row.to_dict()
            
            # Make prediction
            result = client.predict_transaction(transaction)
            
            # Log results
            logger.info(f"Transaction {idx}:")
            logger.info(f"  Amount: ${transaction['amount']:.2f}")
            logger.info(f"  Prediction: {'Fraudulent' if result['prediction'] == 1 else 'Legitimate'}")
            logger.info(f"  Probability: {result['probability']:.4f}")
            logger.info(f"  Timestamp: {result['timestamp']}")
            logger.info("-" * 50)
            
        except Exception as e:
            logger.error(f"Error processing transaction {idx}: {str(e)}")
            continue

if __name__ == "__main__":
    main()
