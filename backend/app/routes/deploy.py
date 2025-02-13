"""
API routes for deployment-related operations.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Deployment, Project
from database import get_db
from schemas import DeploymentCreate, DeploymentResponse
import subprocess
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/deploy", response_model=DeploymentResponse)
def create_deployment(deployment: DeploymentCreate, db: Session = Depends(get_db)):
    """
    Create a deployment for the specified project.

    Args:
        deployment (DeploymentCreate): Deployment creation details.
        db (Session): Database session.

    Returns:
        DeploymentResponse: Created deployment details.
    """
    try:
        project = db.query(Project).filter(Project.id == deployment.project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        
        # Simulate deployment process
        deployment_command = f"echo 'Deploying {project.title}'"
        subprocess.run(deployment_command, shell=True, check=True)

        new_deployment = Deployment(
            project_id=deployment.project_id,
            environment=deployment.environment,
            status="deployed"
        )
        db.add(new_deployment)
        db.commit()
        db.refresh(new_deployment)
        return new_deployment
    except subprocess.CalledProcessError as e:
        logger.error(f"Deployment error: {e}")
        raise HTTPException(status_code=500, detail="Deployment failed")
    except HTTPException as e:
        logger.error(f"HTTP error in create_deployment: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error in create_deployment: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")