# Technical Report: Threat Monitoring & Alert Management System

## 1. Executive Summary

The Threat Monitor System is a modular, high-fidelity security platform designed to ingest, process, and manage security events in real-time. Built with a focus on scalability and production readiness, the system leverages a modern tech stack to provide automated alerting, comprehensive user auditing, and a premium administrative dashboard.

## 2. Technical Architecture

The system follows a container-first architecture, ensuring consistency across development and production environments.

- **Backend**: Django 5.2 (Python 3.11) with Django REST Framework (DRF).
- **Database**: PostgreSQL (Production) / SQLite (Local Development).
- **Server**: Gunicorn (Production Gateway) for handling concurrent requests.
- **Frontend**: Django MVT with Vanilla CSS, responsive design, and live notification polling.
- **Infrastructure**: Docker & Docker Compose for orchestration.

## 3. Key Features

### 3.1 Automated Threat Detection

The system uses Django Signals to monitor incoming events. Any event categorized with 'High' or 'Critical' severity instantly triggers the creation of an automated Alert, notifying security analysts in real-time via the dashboard.

### 3.2 User Activity Auditing (Governance)

Integrity is maintained through a custom auditing module. Every sensitive action—including authentication, registration, and status updates on security incidents—is logged with timestamps, IP addresses, and user-agent details.

### 3.3 Unified API Layer

The API provides a consistent JSON structure for all responses. It includes full JWT authentication, field-level validation, and is documented via Swagger/OpenAPI.

## 4. Security Measures

- **Role-Based Access Control (RBAC)**: Distinct permissions for Admins and Analysts.
- **JWT Authentication**: Secured stateless communication for API endpoints.
- **Environment Isolation**: Sensitive credentials are managed via environment variables and never exposed in version control.

## 5. Deployment Details

The application is deployed live on Render.com, utilizing a Dockerized environment integrated with a managed PostgreSQL instance. Static assets are served via WhiteNoise for optimal performance.

---

**Author**: Vinayagam
**Date**: December 25, 2025
**Project Repository**: [GitHub Link](https://github.com/Zyrvix/threat-monitor-system)
**Live Environment**: [Live Application](https://threat-monitor-system.onrender.com/)
