# Student Management API

A RESTful backend application built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. The project demonstrates CRUD operations, JWT Authentication, password hashing, layered architecture, and environment-based configuration.

---

## Features

- Student CRUD Operations
- User Signup & Login
- JWT Authentication
- Password Hashing using bcrypt
- PostgreSQL Database
- SQLAlchemy ORM
- Layered Architecture
- Environment Variables (.env)
- Interactive Swagger Documentation

---

## Tech Stack

- FastAPI
- Python 3.14
- PostgreSQL
- SQLAlchemy
- Pydantic
- Passlib (bcrypt)
- Python-JOSE (JWT)
- Uvicorn
- python-dotenv

---

## Project Structure

```
Student-Management-API
│
├── app
│   ├── models
│   ├── schemas
│   ├── repositories
│   ├── services
│   ├── routers
│   ├── utils
│   ├── database.py
│   ├── dependencies.py
│   ├── config.py
│   └── main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Architecture

The project follows a layered architecture.

```
Client
   │
   ▼
Router
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Database (PostgreSQL)
```

This separation makes the code modular, reusable, and easy to maintain.

---

## Authentication Flow

1. Create an account using `/signup`
2. Login using `/login`
3. Receive a JWT Access Token
4. Click **Authorize** in Swagger UI
5. Access protected endpoints

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/signup` | Register a new user |
| POST | `/login` | Login and receive JWT |

### Students

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students |
| GET | `/students/{id}` | Get a student |
| POST | `/students` | Create student |
| PUT | `/students/{id}` | Replace student |
| PATCH | `/students/{id}` | Update student |
| DELETE | `/students/{id}` | Delete student |
| GET | `/students/search` | Search students |

---

## Installation

Clone the repository

```bash
git clone https://github.com/kamalinireddy/Student-Management-API.git
```

Move into the project

```bash
cd Student-Management-API
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/student_management
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run the server

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## Database

Database: PostgreSQL

Tables:

- users
- students

---

## 📸 Screenshots

### Swagger UI

> Add a screenshot here

### PostgreSQL Tables

> Add a screenshot here

---

## Concepts Demonstrated

- REST API Development
- CRUD Operations
- PostgreSQL Integration
- SQLAlchemy ORM
- JWT Authentication
- Password Hashing
- Dependency Injection
- Environment Variables
- Layered Architecture
- API Documentation with Swagger

---

## Future Improvements

- Refresh Tokens
- Role-Based Authorization
- Unit Testing
- Docker Support
- CI/CD Pipeline
- GraphQL API
- WebSockets
- Kafka Integration

---

## Author

**A Kamalini Reddy**

GitHub: https://github.com/kamalinireddy