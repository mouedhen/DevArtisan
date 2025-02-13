/**
 * Main application component for DevArtisan.
 */

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import HomePage from './pages/HomePage';
import ProjectPage from './pages/ProjectPage';
import ReviewPage from './pages/ReviewPage';
import DeployPage from './pages/DeployPage';
import SecurityPage from './pages/SecurityPage';
import CompliancePage from './pages/CompliancePage';
import MonitoringPage from './pages/MonitoringPage';

const App = () => {
  return (
    <Router>
      <Header />
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/project/:id" component={ProjectPage} />
        <Route path="/review/:id" component={ReviewPage} />
        <Route path="/deploy/:id" component={DeployPage} />
        <Route path="/security/:id" component={SecurityPage} />
        <Route path="/compliance" component={CompliancePage} />
        <Route path="/monitoring" component={MonitoringPage} />
      </Switch>
    </Router>
  );
};

export default App;