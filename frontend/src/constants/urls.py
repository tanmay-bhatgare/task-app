class Url:
    base_url: str = "http://127.0.0.1:8000"
    task_base_url: str = f"{base_url}/tasks"
    sign_up_url: str = f"{base_url}/users/register"
    sign_in_url: str = f"{base_url}/login"
    create_task_url: str = f"{task_base_url}/create"
    update_task_url: str = f"{task_base_url}/update"
