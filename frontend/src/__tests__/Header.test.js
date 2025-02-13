/**
 * Unit tests for the Header component.
 */

import React from 'react';
import { render } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import Header from '../components/Header';

describe('Header', () => {
  it('should render navigation links', () => {
    render(
      <Router>
        <Header />
      </Router>
    );

    expect(screen.getByText('Home')).toBeInTheDocument();
    expect(screen.getByText('Projects')).toBeInTheDocument();
    expect(screen.getByText('Code Review')).toBeInTheDocument();
    expect(screen.getByText('Deploy')).toBeInTheDocument();
    expect(screen.getByText('Security Analysis')).toBeInTheDocument();
    expect(screen.getByText('Compliance Check')).toBeInTheDocument();
    expect(screen.getByText('Monitoring')).toBeInTheDocument();
  });
});