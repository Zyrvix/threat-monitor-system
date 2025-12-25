# Threat Monitor System

A professional security monitoring and alert management system built with Django and PostgreSQL. This system provides real-time event ingestion, automated threat detection, and comprehensive security auditing.

## 🚀 Features

- **Real-time Event Ingestion**: Process massive security event data streams.
- **Automated Alerts**: Instant alert generation for 'High' and 'Critical' severity events using Django Signals.
- **User Activity Auditing**: Detailed tracking of user actions (Auth, Alerts, events) for governance.
- **Unified API Response**: Consistent JSON structure for all API responses and errors.
- **Admin Dashboard**: Premium dark-mode UI for security analysts to monitor and resolve alerts.

---

## 🛠️ Environment Setup

Before running the project (Docker or Manual), create a `.env` file in the root directory:

```ini
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*

# Database Configuration
USE_POSTGRES=True
DB_NAME=threat_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

## 🐳 How to Run (The Docker Way) - Recommended

This is the easiest way to run the full stack (App + PostgreSQL) locally.

1. **Build and Run**:
   ```bash
   docker-compose up --build
   ```
2. **Access the Application**:
   - Dashboard: `http://localhost:8000/`
   - API: `http://localhost:8000/api/v1/`

_Note: The Docker setup automatically handles database migrations and static files._

---

## 💻 How to Run (The Manual Way)

1. **Prepare Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **Setup Database**:
   ```bash
   python manage.py migrate
   ```
3. **Run Server**:
   ```bash
   python manage.py runserver
   ```

---

## 🧪 Testing the APIs

### Environment URLs

- **Localhost**: `http://127.0.0.1:8000/api/v1`
- **Live (Render)**: `https://threat-monitor-system.onrender.com/api/v1`

### Postman Collections

We provide two collections in the root folder for instant testing:

- `postman_local.json`: Pre-configured for local testing.
- `postman_live.json`: Pre-configured for the live production environment.

**How to use:**

1. Import the collection into Postman.
2. Use the **Auth > Login** request first (uses credentials: `vinayagam` / `qwerty@123`).
3. The collections automatically save the `access_token` for subsequent requests.

### API Documentation

- **Interactive Swagger UI**: `/api/v1/docs/`
- **ReDoc Schema**: `/api/v1/schema/`

---

## 🔍 API Filtering Guide

The API supports advanced results filtering. Use these parameters on the `/events/` or `/alerts/` endpoints:

- **Filter by Severity**: `.../events/?severity=high`
- **Filter by Type**: `.../events/?event_type=intrusion`
- **Filter by Status**: `.../alerts/?status=open`
- **Combined Filters**: `.../events/?severity=low&source_name=Firewall-X`

---

## 🛡️ Admin & Authentication

To access the dashboard or the `/admin/` panel:

- **Username**: `vinayagam`
- **Password**: `qwerty@123`

You can create a new superuser manually via terminal:

```bash
python manage.py createsuperuser
```

---

## ☁️ Deployment (Render.com)

The project is optimized for Render using Docker:

1. Create a **PostgreSQL** instance.
2. Create a **Web Service** using the Docker environment.
3. Add the `DATABASE_URL` environment variable from your Postgres instance to the Web Service settings.

---

_Developed for Cyethack Solutions Pvt Ltd. 2025_
