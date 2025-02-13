/**
 * SecurityPage component for displaying and creating security issues.
 */

import React, { useState } from 'react';
import axios from 'axios';

const SecurityPage = ({ match }) => {
  const projectId = match.params.id;
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [severity, setSeverity] = useState('');
  const [message, setMessage] = useState('');

  const handleCreateSecurityIssue = async () => {
    try {
      const response = await axios.post('/api/security', {
        project_id: projectId,
        title,
        description,
        severity,
      });
      setMessage('Security issue created successfully');
    } catch (error) {
      console.error('Error creating security issue:', error);
      setMessage('Error creating security issue');
    }
  };

  return (
    <div className="security-page">
      <h2>Security Issues</h2>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <input
        type="text"
        placeholder="Severity"
        value={severity}
        onChange={(e) => setSeverity(e.target.value)}
      />
      <button onClick={handleCreateSecurityIssue}>Submit Security Issue</button>
      <p>{message}</p>
    </div>
  );
};

export default SecurityPage;