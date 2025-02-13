"""
Unit tests for the DesignerAgent service.
"""

import pytest
from app.services.designer_agent import DesignerAgent
import os

@pytest.fixture
def designer_agent():
    figma_token = os.getenv("FIGMA_API_TOKEN")
    if not figma_token:
        pytest.skip("FIGMA_API_TOKEN environment variable not set")
    return DesignerAgent(figma_token=figma_token)

def test_create_design(designer_agent):
    description = "Create a web application design"
    design_url = designer_agent.create_design(description)
    assert "figma.com" in design_url