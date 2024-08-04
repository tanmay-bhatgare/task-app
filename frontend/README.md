# GUI Task Manager Application with customtkinter

## Introduction

This project is a GUI-based Task Manager application built using customtkinter and FastAPI for backend. The application allows users to manage tasks efficiently with features such as creating, updating, and deleting tasks. The project is organized with a clear structure for assets, source code, and utility functions.

## Features

- User Authentication (Sign In and Sign Up)
- Task CRUD operations (Create, Read, Update, Delete)
- Custom widgets for enhanced UI
- Organized project structure

## Requirements

- Python 3.11+
- customtkinter
- httpx
- other dependencies (specified in requirements.txt)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tanmay-bhatgare/task-app.git
   cd task-app
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

## Running the Application

1. **Navigate to the frontend directory:**

   ```bash
   cd frontend
   ```

2. **Start the application:**

   ```bash
   python main.py
   ```

## Project Structure

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
