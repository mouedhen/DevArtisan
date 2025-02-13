# API Documentation

## Overview

This document provides an overview of the API endpoints available in the application.

## Endpoints

### Root Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a welcome message.
- **Response:**
  - Status: `200 OK`
  - Body: `{"Hello": "World"}`

### Error Endpoint

- **URL:** `/error`
- **Method:** `GET`
- **Description:** Raises a 404 HTTP exception to demonstrate error handling.
- **Response:**
  - Status: `404 Not Found`
  - Body: `{"detail": "Resource not found"}`

## Running the API

To run the API, use the following command:

```bash
uvicorn backend.app.main:app --reload