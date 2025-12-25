# Threat Monitor System

A backend system built with Django and Django REST Framework for ingesting security events and managing alerts. It includes automated alert generation based on severity and role-based access control.

## Project Features

- User authentication using JWT.
- Role-based access control (Admin and Analyst).
- Security event ingestion API.
- Automatic alert generation for High and Critical severity events.
- Geolocation and device enrichment for ingested events.
- Dashboard for viewing events and managing alerts.
- Activity logging for administrative actions.

## Setup Instructions

### Using Docker (Recommended)

1. Create a .env file in the root directory and add the required variables (see .env.example).
2. Run the following command:
   docker-compose up --build
3. Create a superuser to access the admin panel and dashboard:
   docker-compose exec web python manage.py createsuperuser

### Manual Setup

1. Install dependencies:
   pip install -r requirements.txt
2. Run migrations:
   python manage.py migrate
3. Start the server:
   python manage.py runserver

## API Endpoints

- POST /api/v1/accounts/register/ - User registration
- POST /api/v1/accounts/login/ - Login and get tokens
- POST /api/v1/events/ingest/ - Ingest a security event
- GET /api/v1/alerts/ - List alerts
- PATCH /api/v1/alerts/{id}/ - Update alert status (Admin only)

## Assumptions

- High and Critical severity events always require an alert.
- Analysts have read-only access to alerts for monitoring.
- External IP Geolocation service is available for event enrichment.
- System time is recorded in UTC.

## Technical Details

- Backend: Django, DRF
- Database: PostgreSQL
- Documentation: Swagger/OpenAPI 3.0
- Containerization: Docker, Docker Compose

## Testing

Run the unit tests using:
docker-compose exec web python manage.py test
