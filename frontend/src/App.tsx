import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { CssBaseline, ThemeProvider, createTheme, Typography, Box } from '@mui/material';
import { NavBar } from './components/NavBar';
import AnalyzeTransaction from './pages/AnalyzeTransaction';
import TransactionHistory from './pages/TransactionHistory';
import Dashboard from './pages/Dashboard';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: { main: '#212121' },
    secondary: { main: '#1976d2' },
  },
});

const App: React.FC = () => (
  <ThemeProvider theme={theme}>
    <CssBaseline />
    <Router>
      <Box sx={{ width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 4 }}>
        <Typography variant="h3" fontWeight={700} sx={{ mb: 2, display: 'flex', alignItems: 'center' }}>
          <Box component="span" sx={{ fontSize: 38, mr: 1 }}>🛡️</Box>Credit Card Fraud Detection
        </Typography>
        <NavBar />
      </Box>
      <Routes>
        <Route path="/" element={<AnalyzeTransaction />} />
        <Route path="/history" element={<TransactionHistory />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  </ThemeProvider>
);

export default App;
