import React from 'react';

import { ColorModeContext, useMode } from './theme'
import { CssBaseline, ThemeProvider } from '@mui/material'
import { Routes, Route, BrowserRouter as Router } from 'react-router-dom';

import Topbar from './pages/global/Topbar';
// import SideMenu from './scenes/global/SideMenu';
// import Sidebar from './scenes/global/Sidebar';
import Navbar from './pages/global/Navbar';
// import Header from './pages/global/Navbar';

import Dashboard from './pages/dashboard';
import Team from './pages/team';
import Drivers from './pages/drivers';
import Bookings from './pages/bookings';
import Invoices from './pages/invoices';
import Bar from './pages/bar';
// import Pie from './components/PieGraph';

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
      <div className="content">
          <Router>
            <Navbar />
        {/* <main className='content'> */}
            <Routes>
              <Route path='/' exact element={<Dashboard />} />
              <Route path='/team' exact element={<Team />} />
              <Route path='/drivers' exact element={<Drivers />} />
              <Route path='/bookings' exact  element={<Bookings />} />
              <Route path='/invoices' exact element={<Invoices />} />
            </Routes>
          {/* </main> */}
          </Router>
          {/* <Topbar /> 
          {/* <Routes>
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
            <Route path="/faq" element={<FAQ />} />
          </Routes> */}
      </div>
    </ThemeProvider>
  </ColorModeContext.Provider>

  );
};

export default App;
