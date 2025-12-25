# Threat Monitor System

A professional security monitoring and alert management system built with Django and PostgreSQL.

## Features

- **Real-time Monitoring**: Ingest security events and automatically generate alerts based on severity.
- **User Auditing**: Full audit trail of user actions (login, registration, alert changes).
- **Interactive Dashboard**: Modern dark-mode UI with live notification polling.
- **Production Ready**: Fully Dockerized with Gunicorn and WhiteNoise.

## Quick Start (Docker)

To run the entire system locally using Docker:

1. **Clone the repository**
2. **Create a `.env` file** in the root directory (use `.env.example` as a template).
3. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```
   The application will be available at `http://localhost:8000`.

## Manual Installation

1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # venv\Scripts\activate on Windows
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Migrations & Start Server**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## API Documentation

- **Swagger UI**: `/api/v1/docs/`
- **ReDoc**: `/api/v1/schema/`

## Deployment (Render.com)

This project is optimized for deployment on Render:

1. **PostgreSQL**: Create a new Render PostgreSQL instance.
2. **Web Service**:
   - Environment: `Docker`
   - Plan: `Free`
   - **Environment Variables**: Add `DATABASE_URL` (Internal URL from your Postgres instance).
   - **Docker Command**: `sh -c "python manage.py migrate && gunicorn threat_monitor.wsgi:application --bind 0.0.0.0:8000"`

## Testing

Run the automated test suite:

```bash
python manage.py test
```

---

_Developed for Cyethack Solutions Pvt Ltd._
