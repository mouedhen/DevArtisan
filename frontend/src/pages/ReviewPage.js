/**
 * ReviewPage component for displaying project reviews.
 */

import React, { useState } from 'react';
import axios from 'axios';

const ReviewPage = ({ match }) => {
  const projectId = match.params.id;
  const [reviewer, setReviewer] = useState('');
  const [comments, setComments] = useState('');
  const [status, setStatus] = useState('');
  const [message, setMessage] = useState('');

  const handleCreateReview = async () => {
    try {
      const response = await axios.post('/api/review', {
        project_id: projectId,
        reviewer,
        comments,
        status,
      });
      setMessage('Review created successfully');
    } catch (error) {
      console.error('Error creating review:', error);
      setMessage('Error creating review');
    }
  };

  return (
    <div className="review-page">
      <h2>Project Review</h2>
      <input
        type="text"
        placeholder="Reviewer"
        value={reviewer}
        onChange={(e) => setReviewer(e.target.value)}
      />
      <textarea
        placeholder="Comments"
        value={comments}
        onChange={(e) => setComments(e.target.value)}
      />
      <input
        type="text"
        placeholder="Status"
        value={status}
        onChange={(e) => setStatus(e.target.value)}
      />
      <button onClick={handleCreateReview}>Submit Review</button>
      <p>{message}</p>
    </div>
  );
};

export default ReviewPage;