# Hospital Management System API

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-4.x-darkgreen)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.x-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A fully functional Hospital Management System API built with Django and Django REST Framework.  
This project manages patients, doctors, appointments, medical records, billing, and hospital resources with role-based permissions and scheduling rules.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Complete Folder Structure](#complete-folder-structure)
- [Installation & Setup](#installation--setup)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Sample Request & Response](#sample-request--response)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
The Hospital Management API provides backend functionality for hospitals, enabling CRUD operations for patients, doctors, appointments, medical records, billing, and resource scheduling. It enforces authentication, role-based permissions, appointment overlap prevention, and secure handling of attachments.

---

## Features
- Role-based users (Admin, Doctor, Nurse, Receptionist, Billing)
- Patient CRUD with unique MRN and soft-delete support
- Doctor CRUD with specialties and schedule
- Appointment scheduling with overlap and past-date checks
- Medical records with attachments
- Billing and invoices (optional)
- Filters, search, and pagination
- Audit logging for sensitive actions
- API documentation (Swagger/OpenAPI)

---

## Technologies Used
- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL (recommended for production)
- djangorestframework-simplejwt (JWT)
- django-filter
- drf-yasg or drf-spectacular (API docs)
- Gunicorn, Whitenoise (production)
- django-storages + S3 (optional for media)

---

## Complete Folder Structure
Below is the full, detailed project folder structure you should use for the Capstone — copy this exactly into your repo:

```
hms_project/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── Procfile
├── runtime.txt
├── manage.py
├── scripts/
│   ├── seed_data.py
│   └── create_admin.py
├── media/
│   └── attachments/                # uploaded files (local dev)
├── static/
├── docker/                         # optional docker configs
│   ├── Dockerfile
│   └── docker-compose.yml
├── hms_project/                    # Django project package
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   └── celery.py                   # optional (if using Celery)
├── users/                          # staff users, auth
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── tests/
│   │   ├── test_models.py
│   │   ├── test_views.py
│   │   └── test_permissions.py
│   └── migrations/
├── patients/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── filters.py
│   ├── permissions.py
│   ├── tests/
│   └── migrations/
├── doctors/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── filters.py
│   ├── permissions.py
│   ├── tests/
│   └── migrations/
├── appointments/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── validators.py                # appointment overlap validation
│   ├── filters.py
│   ├── permissions.py
│   ├── utils.py                     # scheduling helpers
│   ├── tests/
│   └── migrations/
├── records/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                    # MedicalRecord, Attachment
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── storage_backends.py          # optional S3 storage config
│   ├── tests/
│   └── migrations/
├── attachments/                     # (optional split app)
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── billing/                         # optional
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   └── tests/
├── resources/                       # e.g., OperatingRoom, LabSlot
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── validators.py
│   └── tests/
├── audit/                           # audit logs
│   ├── __init__.py
│   ├── models.py
│   ├── admin.py
│   └── signals.py
├── common/                          # shared utilities
│   ├── __init__.py
│   ├── utils.py
│   ├── mixins.py
│   ├── pagination.py
│   ├── filters.py
│   └── permissions.py
└── docs/
    ├── ERD.png
    ├── API_DOCUMENTATION.md
    └── design_decisions.md
```

---

## Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/hms_project.git
cd hms_project
```

### 2. Create virtualenv & activate
```bash
virtualenv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows (PowerShell)
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
Copy `.env.example` to `.env` and fill in credentials:
```
SECRET_KEY=your-secret
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run migrations & create superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Start server
```bash
python manage.py runserver
```

---

## API Endpoints
**Auth**
```
POST /api/auth/token/         # obtain JWT
POST /api/auth/token/refresh/ # refresh token
POST /api/auth/register/      # create staff user (Admin only)
```

**Patients**
```
GET    /api/patients/
POST   /api/patients/
GET    /api/patients/{id}/
PUT    /api/patients/{id}/
DELETE /api/patients/{id}/
```

**Doctors**
```
GET    /api/doctors/
POST   /api/doctors/
GET    /api/doctors/{id}/
PUT    /api/doctors/{id}/
```

**Appointments**
```
GET    /api/appointments/
POST   /api/appointments/
GET    /api/appointments/{id}/
PUT    /api/appointments/{id}/
DELETE /api/appointments/{id}/
GET    /api/appointments/upcoming/
```

**Records & Attachments**
```
GET  /api/patients/{id}/records/
POST /api/patients/{id}/records/
GET  /api/records/{id}/
POST /api/attachments/
GET  /api/attachments/{id}/
```

---

## Sample Request & Response

### Create Patient
**Request**
```
POST /api/patients/
Authorization: Bearer <ACCESS_TOKEN>
Content-Type: application/json

{
  "first_name": "Mary",
  "last_name": "Kintu",
  "date_of_birth": "1985-02-15",
  "gender": "female",
  "contact_phone": "0771234567",
  "contact_email": "mary@example.com",
  "address": "Kampala, Uganda",
  "emergency_contact": "John Kintu - 0777654321"
}
```

**Response (201)**
```json
{
  "id": 1,
  "first_name": "Mary",
  "last_name": "Kintu",
  "medical_record_number": "a1b2c3d4",
  "created_at": "2025-12-06T12:00:00Z"
}
```

---

## Running Tests
Run all tests:
```bash
python manage.py test
```

Run a single app tests (example):
```bash
python manage.py test appointments
```

---

## Deployment
- Prepare `Procfile`, `runtime.txt`, and `requirements.txt`.
- Use PostgreSQL in production. Set `DATABASE_URL` env var.
- Configure `ALLOWED_HOSTS`, `DEBUG=False`, and secure settings.
- Use S3 (django-storages) for media files.
- Example (Heroku):
  ```bash
  heroku create your-app-name
  git push heroku main
  heroku config:set SECRET_KEY='...'
  heroku addons:create heroku-postgresql:hobby-dev
  heroku run python manage.py migrate
  heroku run python manage.py createsuperuser
  ```

---

## Security Notes
- Protect PHI with role-based permissions.
- Enforce HTTPS in production.
- Do not log sensitive data.
- Use signed URLs or protected endpoints for attachments.

---

## Contributing
1. Fork the repo
2. Create a feature branch
3. Write tests for new features
4. Open a Pull Request

---

## License
MIT License
