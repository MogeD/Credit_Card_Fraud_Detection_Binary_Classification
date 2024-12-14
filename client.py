import pandas as pd
import requests
import json

# Load the OOS data (assuming it's stored as 'oos_data.csv')
oos_data = pd.read_csv('oos_data.csv')

# Extract the actual values for your features from the first row of OOS data
actual_values = {
    "Net Income to Stockholder s Equity": oos_data["Net Income to Stockholder s Equity"].iloc[0],
    "Net Value Growth Rate": oos_data["Net Value Growth Rate"].iloc[0],
    "Degree of Financial Leverage  DFL": oos_data["Degree of Financial Leverage  DFL"].iloc[0],
    "Per Share Net profit before tax  Yuan": oos_data["Per Share Net profit before tax  Yuan"].iloc[0],
    "Net Value Per Share  A": oos_data["Net Value Per Share  A"].iloc[0],
    "Net Income to Total Assets": oos_data["Net Income to Total Assets"].iloc[0],
    "Interest Coverage Ratio  Interest expense to EBIT": oos_data["Interest Coverage Ratio  Interest expense to EBIT"].iloc[0],
    "Net worth Assets": oos_data["Net worth Assets"].iloc[0],
}

# Print the actual feature values
print("Actual OOS Feature Values:", actual_values)

# The URL of your FastAPI server
url = "http://127.0.0.1:8000/predict"

# Send a POST request with the actual values
response = requests.post(url, json=actual_values)

# Check if the request was successful
if response.status_code == 200:
    # Print the prediction result from the server
    print("Prediction:", response.json())
else:
    print("Error:", response.status_code)
