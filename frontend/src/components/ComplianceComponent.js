import React from 'react';

function ComplianceComponent({ check }) {
    return (
        <div>
            <h2>{check.name}</h2>
            <p>Status: {check.status}</p>
            <p>Created At: {new Date(check.created_at).toLocaleString()}</p>
        </div>
    );
}

export default ComplianceComponent;