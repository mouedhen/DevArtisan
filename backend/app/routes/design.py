"""
API routes for design-related operations.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Project
from database import get_db
from schemas import ProjectCreate, ProjectResponse
from services.designer_agent import DesignerAgent
import os
import logging

logger = logging.getLogger(__name__)

router = APIRouter()
figma_token = os.getenv("FIGMA_API_TOKEN")

designer_agent = DesignerAgent(figma_token=figma_token)

@router.post("/design", response_model=ProjectResponse)
def create_design(project: ProjectCreate, db: Session = Depends(get_db)):
    """
    Create a design based on the project description.

    Args:
        project (ProjectCreate): Project creation details.
        db (Session): Database session.

    Returns:
        ProjectResponse: Created project details.
    """
    if not figma_token:
        logger.warning("Figma API token not provided. DesignerAgent is disabled.")
        raise HTTPException(status_code=400, detail="Figma API token not provided.")
    
    try:
        if not project.description:
            raise HTTPException(status_code=400, detail="Project description is required")
        design_url = designer_agent.create_design(project.description)
        new_project = Project(title=project.title, description=project.description, plan=design_url)
        db.add(new_project)
        db.commit()
        db.refresh(new_project)
        return new_project
    except HTTPException as e:
        logger.error(f"HTTP error in create_design: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error in create_design: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")