# Task Manager Backend with FastAPI

## Introduction

This project is a backend application for a Task Manager built using FastAPI. It provides a RESTful API for managing tasks, users, and other related entities. The application uses PostgreSQL as the database and Pydantic for data validation.

## Features

- User Authentication and Authorization
- Task CRUD operations (Create, Read, Update, Delete)
- User and Task management
- JWT-based authentication
- Pydantic models for data validation

## Requirements

- Python 3.11+
- FastAPI
- PostgreSQL
- Pydantic
- SQLAlchemy
- Alembic
- Uvicorn
- Passlib (for password hashing)
- jose (for JWT tokens)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/task-manager-backend.git
   cd task-manager-backend
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Change the directory:**

   ```bash
   cd ./backend/
   ```

5. **Set up the database:**

   Create a PostgreSQL database and configure the database URL in the `.env` file with following attributes.

   ```env
   DATABASE_HOSTNAME={host on which your DB is serving}  # localhost by default
   DATABASE_PORT={port on which your DB is serving}      # 5432 by default
   DATABASE_PASSWORD={password for your DB}
   DATABASE_NAME={name of DB you made}
   DATABASE_USERNAME={username of your database}         # postgres by default from PgAdmin
   SECRET_KEY={secret key for protecting your OAuth login credentials}
   ALGORITHMS={algorithm used for authentication token}
   ACCESS_TOKEN_EXPIRE_MINUTES={number of minutes to expire a login token}  # 60 mins by default
   ```

## Running the Application

1. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## Project Structure

```bash
    backend
    │   └── app
    │       ├── _init_.py
    │       ├── authentication
    │       │   ├── _init_.py
    │       │   └── oauth2.py
    │       ├── configuration
    │       │   └── config.py
    │       ├── db
    │       │   ├── _init_.py
    │       │   └── database.py
    │       ├── main.py
    │       ├── models
    │       │   ├── _init_.py
    │       │   ├── taskModel.py
    │       │   └── userModel.py
    │       ├── routes
    │       │   ├── authRoutes.py
    │       │   ├── taskRoutes.py
    │       │   └── userRoutes.py
    │       ├── schemas
    │       │   ├── _init_.py
    │       │   ├── taskSchema.py
    │       │   ├── tokenSchema.py
    │       │   └── userSchema.py
    │       └── utils
    │           ├── _init_.py
    │           └── utils.py
```
