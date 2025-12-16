# Marketplace Web Application

A full-stack marketplace web application that enables users to create accounts, browse product listings, and manage marketplace interactions through a web-based interface.

This project was developed as part of a software engineering course and follows a modular, production-style architecture with containerization and CI/CD workflows.

## Tech Stack

- Backend: Python, Flask  
- Frontend: React, JavaScript, HTML, CSS  
- Database: SQLite  
- DevOps: Docker, GitHub Actions (CI/CD)  
- Design & Planning: Figma, Trello  

## System Architecture

- 3-tier architecture consisting of:
  - React single-page application (frontend)
  - Flask REST API (backend)
  - SQLite relational database
- Backend services containerized using Docker
- Automated CI/CD workflows for linting, testing, and build validation using GitHub Actions
- Clear API contracts and separation of concerns between frontend and backend

## Key Features

- User account creation and authentication
- Product listing and browsing functionality
- Database-backed API endpoints
- Dockerized frontend and backend services
- CI/CD pipelines triggered on push and pull requests

## My Contributions

- Implemented backend API endpoints using Flask
- Integrated SQLite database with backend services
- Built and configured CI/CD pipelines using GitHub Actions (YAML workflows)
- Containerized backend services using Docker
- Created API contracts and architecture diagrams to guide system integration

## How to Run the Application

### Prerequisites
- Docker Desktop installed and running

### Running the Backend

cd backend
docker build -t backend .
docker run -p 5001:5001 backend

### Running the Frontend
cd frontend
docker build -t frontend .
docker run -p 5173:5173 frontend

Open your browser and navigate to:
http://localhost:5173



