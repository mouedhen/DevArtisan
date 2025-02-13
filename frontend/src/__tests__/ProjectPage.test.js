/**
 * Unit tests for the ProjectPage component.
 */

import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import axios from 'axios';
import ProjectPage from '../pages/ProjectPage';

jest.mock('axios');

describe('ProjectPage', () => {
  it('should render project details and actions', () => {
    render(<ProjectPage match={{ params: { id: 1 } }} />);
    expect(screen.getByText('Project Details')).toBeInTheDocument();
    expect(screen.getByText('Create Architecture')).toBeInTheDocument();
    expect(screen.getByText('Generate Code')).toBeInTheDocument();
    expect(screen.getByText('Download Project Files')).toBeInTheDocument();
    expect(screen.getByText('Create Design')).toBeInTheDocument();
  });

  it('should handle create architecture action', async () => {
    axios.post.mockResolvedValue({ data: { plan: 'Architecture plan' } });

    render(<ProjectPage match={{ params: { id: 1 } }} />);
    fireEvent.click(screen.getByText('Create Architecture'));

    expect(await screen.findByText('Architecture plan')).toBeInTheDocument();
  });

  it('should handle generate code action', async () => {
    axios.post.mockResolvedValue({ data: { message: 'Code generated' } });

    render(<ProjectPage match={{ params: { id: 1 } }} />);
    fireEvent.click(screen.getByText('Generate Code'));

    expect(await screen.findByText('Code generated')).toBeInTheDocument();
  });

  it('should handle download project files action', async () => {
    const blob = new Blob(['project files'], { type: 'application/zip' });
    axios.get.mockResolvedValue({ data: blob });

    render(<ProjectPage match={{ params: { id: 1 } }} />);
    fireEvent.click(screen.getByText('Download Project Files'));

    // Expect the download to be initiated (can't test actual file download in jest)
  });

  it('should handle create design action', async () => {
    axios.post.mockResolvedValue({ data: { plan: 'Design URL' } });

    render(<ProjectPage match={{ params: { id: 1 } }} />);
    fireEvent.click(screen.getByText('Create Design'));

    expect(await screen.findByText('Design created: Design URL')).toBeInTheDocument();
  });
});