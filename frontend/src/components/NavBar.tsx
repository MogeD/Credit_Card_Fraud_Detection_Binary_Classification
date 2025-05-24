import React from 'react';
import { AppBar, Tabs, Tab, Toolbar, Typography, Box } from '@mui/material';
import { useLocation, useNavigate } from 'react-router-dom';

const tabs = [
  { label: 'Analyze Transaction', path: '/' },
  { label: 'Transaction History', path: '/history' },
  { label: 'Dashboard', path: '/dashboard' },
];

export const NavBar: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const currentTab = tabs.findIndex(tab => tab.path === location.pathname) !== -1
    ? tabs.findIndex(tab => tab.path === location.pathname)
    : 0;

  return (
    <Box sx={{ width: '100%', display: 'flex', justifyContent: 'center', mt: 4, mb: 4 }}>
      <Box sx={{ width: 900, bgcolor: '#fafbfc', borderRadius: 2, boxShadow: 1 }}>
        <Tabs
          value={currentTab}
          onChange={(_, v) => navigate(tabs[v].path)}
          TabIndicatorProps={{ style: { display: 'none' } }}
          sx={{
            minHeight: 48,
            '& .MuiTab-root': {
              minHeight: 48,
              fontWeight: 600,
              fontSize: 18,
              borderRadius: 2,
              mx: 0.5,
              textTransform: 'none',
            },
            '& .Mui-selected': {
              bgcolor: '#fff',
              color: '#111',
              boxShadow: 1,
            },
            '& .MuiTabs-flexContainer': {
              justifyContent: 'center',
            },
          }}
        >
          {tabs.map(tab => (
            <Tab key={tab.path} label={tab.label} />
          ))}
        </Tabs>
      </Box>
    </Box>
  );
}; 