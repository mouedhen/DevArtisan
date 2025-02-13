"""
DesignerAgent service for generating design elements and communicating with the Figma API.
"""

import requests
import json
import logging

logger = logging.getLogger(__name__)

class DesignerAgent:
    def __init__(self, figma_token: str = None):
        """
        Initialize the DesignerAgent with the Figma API token.
        """
        self.figma_token = figma_token
        self.base_url = "https://api.figma.com/v1"

    def create_design(self, description: str) -> str:
        """
        Create a design based on the provided description.

        Args:
            description (str): Description of the design.

        Returns:
            str: URL of the created Figma file.
        """
        if not self.figma_token:
            logger.warning("Figma API token not provided. DesignerAgent is disabled.")
            raise ValueError("Figma API token not provided.")
        
        try:
            design_elements = self._generate_design_elements(description)
            figma_file_url = self._create_figma_file(design_elements)
            return figma_file_url
        except Exception as e:
            logger.error(f"Error creating design: {e}")
            raise

    def _generate_design_elements(self, description: str) -> dict:
        """
        Generate design elements based on the description.

        Args:
            description (str): Description of the design.

        Returns:
            dict: Generated design elements.
        """
        try:
            # Here we would use an AI service to generate design elements based on the description
            # For the sake of this example, we'll simulate this with static data
            return {
                "name": "Generated Design",
                "elements": [
                    {"type": "rectangle", "width": 100, "height": 100, "color": "#FF0000"},
                    {"type": "text", "content": "Hello, World!", "fontSize": 24}
                ]
            }
        except Exception as e:
            logger.error(f"Error generating design elements: {e}")
            raise

    def _create_figma_file(self, design_elements: dict) -> str:
        """
        Create a Figma file with the generated design elements.

        Args:
            design_elements (dict): Generated design elements.

        Returns:
            str: URL of the created Figma file.
        """
        try:
            headers = {
                "X-Figma-Token": self.figma_token,
                "Content-Type": "application/json"
            }
            data = {
                "name": design_elements["name"],
                "components": design_elements["elements"]
            }
            response = requests.post(f"{self.base_url}/files", headers=headers, data=json.dumps(data))
            response.raise_for_status()
            figma_file_url = response.json().get("url")
            return figma_file_url
        except requests.RequestException as e:
            logger.error(f"Error communicating with Figma API: {e}")
            raise
        except Exception as e:
            logger.error(f"Error creating Figma file: {e}")
            raise