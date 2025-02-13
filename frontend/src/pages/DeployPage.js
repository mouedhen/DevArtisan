/**
 * DeployPage component for managing deployments.
 */

import React, { useState } from 'react';
import axios from 'axios';

const DeployPage = ({ match }) => {
  const projectId = match.params.id;
  const [environment, setEnvironment] = useState('');
  const [message, setMessage] = useState('');

  const handleCreateDeployment = async () => {
    try {
      const response = await axios.post('/api/deploy', {
        project_id: projectId,
        environment,
      });
      setMessage('Deployment created successfully');
    } catch (error) {
      console.error('Error creating deployment:', error);
      setMessage('Error creating deployment');
    }
  };

  return (
    <div className="deploy-page">
      <h2>Deploy Project</h2>
      <input
        type="text"
        placeholder="Environment"
        value={environment}
        onChange={(e) => setEnvironment(e.target.value)}
      />
      <button onClick={handleCreateDeployment}>Submit Deployment</button>
      <p>{message}</p>
    </div>
  );
};

export default DeployPage;