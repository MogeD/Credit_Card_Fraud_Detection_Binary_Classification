import React from 'react';
import { Box, Typography } from '@mui/material';

const TransactionHistory: React.FC = () => (
  <Box sx={{ p: 4, textAlign: 'center' }}>
    <Typography variant="h5">Transaction History</Typography>
    <Typography variant="body1" sx={{ mt: 2 }}>
      This is a placeholder for the transaction history page.
    </Typography>
  </Box>
);

export default TransactionHistory; 