import React, { useState } from 'react';
import {
    Box,
    Button,
    TextField,
    Typography,
    Paper,
    Alert,
    CircularProgress,
    MenuItem,
    InputAdornment
} from '@mui/material';
import { TransactionFeatures } from '../types';
import { api } from '../services/api';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';

const initialTransaction: TransactionFeatures = {
    time: 0,
    amount: 0,
    v1: 0,
    v2: 0,
    v3: 0,
    v4: 0,
    v5: 0,
    v6: 0,
    v7: 0,
    v8: 0,
    v9: 0,
    v10: 0,
    v11: 0,
    v12: 0,
    v13: 0,
    v14: 0,
    v15: 0,
    v16: 0,
    v17: 0,
    v18: 0,
    v19: 0,
    v20: 0,
    v21: 0,
    v22: 0,
    v23: 0,
    v24: 0,
    v25: 0,
    v26: 0,
    v27: 0,
    v28: 0
};

const merchantTypes = [
    'Grocery', 'Electronics', 'Clothing', 'Restaurant', 'Travel', 'Other'
];

export const TransactionForm: React.FC = () => {
    const [transaction, setTransaction] = useState<TransactionFeatures>(initialTransaction);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [result, setResult] = useState<{ prediction: number; probability: number } | null>(null);
    const [merchantType, setMerchantType] = useState('');
    const [location, setLocation] = useState('');
    const [transactionTime, setTransactionTime] = useState<Date | null>(null);
    const [cardholderName, setCardholderName] = useState('');
    const [cardLast4, setCardLast4] = useState('');

    const handleInputChange = (field: keyof TransactionFeatures) => (
        event: React.ChangeEvent<HTMLInputElement>
    ) => {
        const value = parseFloat(event.target.value);
        setTransaction(prev => ({
            ...prev,
            [field]: isNaN(value) ? 0 : value
        }));
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setLoading(true);
        setError(null);
        setResult(null);

        try {
            const response = await api.predictTransaction(transaction);
            setResult({
                prediction: response.prediction,
                probability: response.probability
            });
        } catch (err) {
            setError('Error making prediction. Please try again.');
            console.error('Prediction error:', err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box sx={{ width: '100%', display: 'flex', justifyContent: 'center', mt: 4 }}>
            <Paper elevation={3} sx={{ p: 4, maxWidth: 600, width: '100%', borderRadius: 3, boxShadow: 2 }}>
                <Typography variant="h5" fontWeight={700} sx={{ mb: 1 }}>
                    Analyze Transaction
                </Typography>
                <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
                    Enter transaction details to check for potential fraud
                </Typography>
                <form onSubmit={handleSubmit}>
                    <Box sx={{
                        display: 'grid',
                        gridTemplateColumns: { xs: '1fr', sm: '1fr 1fr' },
                        gap: 2,
                        mb: 2
                    }}>
                        <TextField
                            fullWidth
                            label="Transaction Amount"
                            type="number"
                            value={transaction.amount}
                            onChange={handleInputChange('amount')}
                            InputProps={{
                                startAdornment: <InputAdornment position="start">$</InputAdornment>
                            }}
                            required
                        />
                        <TextField
                            select
                            fullWidth
                            label="Merchant Type"
                            value={merchantType}
                            onChange={e => setMerchantType(e.target.value)}
                            required
                        >
                            <MenuItem value="">Select merchant type</MenuItem>
                            {merchantTypes.map(type => (
                                <MenuItem key={type} value={type}>{type}</MenuItem>
                            ))}
                        </TextField>
                        <TextField
                            fullWidth
                            label="Transaction Location"
                            value={location}
                            onChange={e => setLocation(e.target.value)}
                            placeholder="City, Country"
                        />
                        <LocalizationProvider dateAdapter={AdapterDateFns}>
                          <DateTimePicker
                            label="Transaction Time"
                            value={transactionTime}
                            onChange={setTransactionTime}
                            slotProps={{ textField: { fullWidth: true } }}
                          />
                        </LocalizationProvider>
                        <TextField
                            fullWidth
                            label="Cardholder Name"
                            value={cardholderName}
                            onChange={e => setCardholderName(e.target.value)}
                            placeholder="John Doe"
                        />
                        <TextField
                            fullWidth
                            label="Card Last 4 Digits"
                            value={cardLast4}
                            onChange={e => setCardLast4(e.target.value.replace(/[^0-9]/g, '').slice(0, 4))}
                            placeholder="1234"
                            inputProps={{ maxLength: 4 }}
                            helperText="Last 4 digits of the credit card"
                        />
                    </Box>
                    <Button
                        type="submit"
                        variant="contained"
                        color="primary"
                        disabled={loading}
                        sx={{ width: '100%', fontWeight: 700, fontSize: 18, mt: 2, py: 1.5 }}
                    >
                        {loading ? <CircularProgress size={24} /> : 'Analyze Transaction'}
                    </Button>
                </form>

                {error && (
                    <Alert severity="error" sx={{ mt: 2 }}>
                        {error}
                    </Alert>
                )}

                {result && (
                    <Box sx={{ mt: 3 }}>
                        <Alert
                            severity={result.prediction === 1 ? 'error' : 'success'}
                            sx={{ mb: 2 }}
                        >
                            {result.prediction === 1
                                ? 'Fraudulent Transaction Detected!'
                                : 'Legitimate Transaction'}
                        </Alert>
                        <Typography variant="body1">
                            Probability of fraud: {(result.probability * 100).toFixed(2)}%
                        </Typography>
                    </Box>
                )}
            </Paper>
        </Box>
    );
}; 