"""
API routes for project-related operations.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Project
from database import get_db
from schemas import ProjectCreate, ProjectResponse
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/plan", response_model=ProjectResponse)
def generate_project_plan(project: ProjectCreate, db: Session = Depends(get_db)):
    """
    Generate a project plan based on the provided project details.

    Args:
        project (ProjectCreate): Project creation details.
        db (Session): Database session.

    Returns:
        ProjectResponse: Created project details with plan.
    """
    try:
        if not project.description:
            raise HTTPException(status_code=400, detail="Project description is required")
        
        # Simulate project plan generation
        project_plan = f"Generated project plan for '{project.title}': {project.description}"
        
        # Save the project plan to the database
        new_project = Project(title=project.title, description=project.description, plan=project_plan)
        db.add(new_project)
        db.commit()
        db.refresh(new_project)
        return new_project
    except HTTPException as e:
        logger.error(f"HTTP error in generate_project_plan: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error in generate_project_plan: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/generate-code/{project_id}", response_model=dict)
def generate_code(project_id: int, db: Session = Depends(get_db)):
    """
    Generate code for the specified project.

    Args:
        project_id (int): ID of the project.
        db (Session): Database session.

    Returns:
        dict: Message indicating the status of the code generation.
    """
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        
        # Simulate code generation
        code_directory = f"generated_code/{project.title.replace(' ', '_')}"
        os.makedirs(code_directory, exist_ok=True)
        with open(f"{code_directory}/main.py", "w") as f:
            f.write("# Generated code\n")
            f.write("print('Hello, World!')\n")
        
        return {"message": "Code generated and saved successfully"}
    except HTTPException as e:
        logger.error(f"HTTP error in generate_code: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error in generate_code: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")