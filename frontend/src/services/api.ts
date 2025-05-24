import axios from 'axios';
import { TransactionFeatures, PredictionResponse } from '../types';

const API_BASE_URL = 'http://localhost:8000';

export const api = {
    async checkHealth(): Promise<{ status: string; timestamp: string }> {
        const response = await axios.get(`${API_BASE_URL}/health`);
        return response.data;
    },

    async predictTransaction(transaction: TransactionFeatures): Promise<PredictionResponse> {
        const response = await axios.post(`${API_BASE_URL}/predict`, transaction);
        return response.data;
    }
}; 