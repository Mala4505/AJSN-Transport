import React from 'react';

import { ColorModeContext, useMode } from './theme'
import { CssBaseline, ThemeProvider } from '@mui/material'
import { Routes, Route } from 'react-router-dom';

import Topbar from './scenes/global/Topbar';
// import SideMenu from './scenes/global/SideMenu';
import Navbar from './scenes/global/Navbar';

import Dashboard from './scenes/dashboard';
import Team from './scenes/team';
import Drivers from './scenes/drivers';
import Bookings from './scenes/bookings';
import Invoices from './scenes/invoices';
import Bar from './scenes/bar';
import Pie from './components/PieGraph';

// import Form from './scenes/form';
// import Line from './scenes/line';
// import Pie from './scenes/pie';
// import Calendar from './scenes/contacts';
// import FAQ from './scenes/faq';



function App() {
  const [theme, colorMode] = useMode();

  return (
  <ColorModeContext.Provider value={colorMode}>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <div className="app">
        <Navbar />
        <main className='content'>
          <Topbar />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/team" element={<Team />} />
            <Route path="/drivers" element={<Drivers />} />
            <Route path="/bookings" element={<Bookings />} />
            <Route path="/invoices" element={<Invoices />} />
            <Route path="/bar" element={<Bar />} />
            <Route path="/pie" element={<Pie />} />
            {/* <Route path="/form" element={<Form />} />
            <Route path="/line" element={<Line />} />
            <Route path="/calendar" element={<Calendar />} />
            <Route path="/faq" element={<FAQ />} /> */}
          </Routes>
        </main>
      </div>
    </ThemeProvider>
  </ColorModeContext.Provider>

  );
};

export default App;
