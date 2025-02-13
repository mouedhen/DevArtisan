/**
 * ProjectPage component for displaying project details and actions.
 */

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProjectPage = ({ match }) => {
  const projectId = match.params.id;
  const [message, setMessage] = useState('');
  const [collaborationMessage, setCollaborationMessage] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:8000/ws/${projectId}`);
    ws.onmessage = (event) => {
      setCollaborationMessage(event.data);
    };
    setSocket(ws);

    return () => {
      ws.close();
    };
  }, [projectId]);

  const handleCreateArchitecture = async () => {
    try {
      const response = await axios.post(`/api/architecture/architecture`, { project_id: projectId });
      setMessage(response.data.plan);
    } catch (error) {
      console.error('Error creating architecture:', error);
      setMessage('Error creating architecture');
    }
  };

  const handleGenerateCode = async () => {
    try {
      const response = await axios.post(`/api/project/generate-code/${projectId}`);
      setMessage(response.data.message);
    } catch (error) {
      console.error('Error generating code:', error);
      setMessage('Error generating code');
    }
  };

  const handleDownload = async () => {
    try {
      const response = await axios.get(`/api/project/download/${projectId}`, {
        responseType: 'blob',
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `project_${projectId}.zip`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error('Error downloading project files:', error);
      setMessage('Error downloading project files');
    }
  };

  const handleCreateDesign = async () => {
    try {
      const response = await axios.post(`/api/design`, { title: "Test Project", description: "Create a web application design" });
      setMessage(`Design created: ${response.data.plan}`);
    } catch (error) {
      console.error('Error creating design:', error);
      setMessage('Error creating design');
    }
  };

  const sendCollaborationMessage = () => {
    if (socket) {
      socket.send(`New collaboration message for project ${projectId}`);
    }
  };

  return (
    <div className="project-page">
      <h2>Project Details</h2>
      <button onClick={handleCreateArchitecture}>Create Architecture</button>
      <button onClick={handleGenerateCode}>Generate Code</button>
      <button onClick={handleDownload}>Download Project Files</button>
      <button onClick={handleCreateDesign}>Create Design</button>
      <button onClick={sendCollaborationMessage}>Send Collaboration Message</button>
      <p>{message}</p>
      <p>{collaborationMessage}</p>
    </div>
  );
};

export default ProjectPage;