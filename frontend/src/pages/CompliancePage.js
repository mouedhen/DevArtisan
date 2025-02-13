import React, { useState, useEffect } from 'react';
import ComplianceComponent from '../components/ComplianceComponent';

function CompliancePage() {
    const [complianceChecks, setComplianceChecks] = useState([]);

    useEffect(() => {
        fetch('/compliance')
            .then(response => response.json())
            .then(data => setComplianceChecks(data))
            .catch(error => console.error('Error fetching compliance checks:', error));
    }, []);

    return (
        <div>
            <h1>Compliance Checks</h1>
            {complianceChecks.map(check => (
                <ComplianceComponent key={check.id} check={check} />
            ))}
        </div>
    );
}

export default CompliancePage;