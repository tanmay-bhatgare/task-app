# Full Stack GUI Task Manager Application with customtkinter (Frontend) and FastAPI (Backend)

## Introduction

This project is a full stack Task Manager application. The frontend is built using customtkinter, and the backend is built using FastAPI. The application allows users to manage tasks efficiently with features such as creating, updating, and deleting tasks, along with user authentication.

## Features

- User Authentication and Authorization
- Task CRUD operations (Create, Read, Update, Delete)
- User and Task management
- JWT-based authentication
- Pydantic models for data validation
- Custom widgets for enhanced UI

## Requirements

### Frontend

- Python 3.11+
- customtkinter
- requests
- other dependencies (specified in `requirements.txt`)

### Backend

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

1. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install the backend dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**

   Create a PostgreSQL database and configure the database URL in the `.env` in .\backend\ file with the following attributes:

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

### Frontend

1. **Navigate to the frontend directory:**

   ```bash
   cd frontend
   ```

2. **Start the frontend application:**

   ```bash
   python main.py
   ```

   The GUI will be available locally.

### Backend

1. **Navigate to the backend directory:**

   ```bash
   cd backend
   ```

2. **Start the FastAPI server:**

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## Project Structure

### Frontend

```bash

frontend
    ├── _init_.py
    ├── assets
    │   └── images
    │       ├── hide.png
    │       └── view.png
    ├── main.py
    └── src
        ├── _init_.py
        ├── app.py
        ├── app_state.py
        ├── constants
        │   ├── _init_.py
        │   ├── c_fonts.py
        │   ├── constants.py
        │   ├── pages.py
        │   ├── paths.py
        │   ├── unit_attributes.py
        │   └── urls.py
        ├── models
        │   ├── _init_.py
        │   ├── models.py
        │   ├── sign_in_user_model.py
        │   ├── sign_up_user_model.py
        │   ├── task_create_model.py
        │   └── task_update_model.py
        ├── pages
        │   ├── about_page.py
        │   ├── create_task_page.py
        │   ├── error_page.py
        │   ├── home_page.py
        │   ├── pages.py
        │   ├── sign_in_page.py
        │   ├── sign_up_page.py
        │   └── update_task_page.py
        ├── services
        │   ├── _init_.py
        │   ├── create_task.py
        │   ├── get_all_tasks.py
        │   ├── services.py
        │   ├── sign_in.py
        │   ├── sign_up.py
        │   └── update_task.py
        ├── tests
        │   └── test.py
        ├── utils
        │   ├── _init_.py
        │   ├── date_parser.py
        │   └── utils.py
        └── widgets
            ├── c_button.py
            ├── c_calendar.py
            ├── c_frame.py
            ├── c_image.py
            ├── c_input_field.py
            ├── c_label.py
            ├── c_option_menu.py
            ├── c_scrollable_frame.py
            ├── c_seperator.py
            ├── c_task_card.py
            └── widget.py
```

### Backend

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
