import React from 'react';
import { Box, Typography } from '@mui/material';

const Dashboard: React.FC = () => (
  <Box sx={{ p: 4, textAlign: 'center' }}>
    <Typography variant="h5">Dashboard</Typography>
    <Typography variant="body1" sx={{ mt: 2 }}>
      This is a placeholder for the dashboard page.
    </Typography>
  </Box>
);

export default Dashboard; 