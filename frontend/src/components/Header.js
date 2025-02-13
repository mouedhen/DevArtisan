/**
 * Header component for the DevArtisan application.
 */

import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="header">
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/project">Projects</Link></li>
          <li><Link to="/review">Code Review</Link></li>
          <li><Link to="/deploy">Deploy</Link></li>
          <li><Link to="/security">Security Analysis</Link></li>
          <li><Link to="/compliance">Compliance Check</Link></li>
          <li><Link to="/monitoring">Monitoring</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;