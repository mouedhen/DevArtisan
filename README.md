# DevArtisan

DevArtisan is an AI-powered platform that assists developers in generating project plans, designs, and code. It integrates with Figma for design generation and provides a complete CI/CD pipeline for automated testing, building, and deployment.

## Features

- **Project Planning**: Generate detailed project plans based on user input.
- **Design Generation**: Create design elements and Figma files based on descriptions.
- **Code Generation**: Automatically generate code for projects.
- **CI/CD Pipeline**: Automated testing, building, and deployment.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [Platform Architecture](#platform-architecture)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Getting Started

### Prerequisites

- Python 3.9
- Node.js 14
- Docker
- Figma API token (optional)
- Git

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mouedhen/devartisan.git
    cd devartisan
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application:
```bash
uvicorn backend.app.main:app --reload