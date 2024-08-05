class AppState:
    def __init__(self):
        self.access_token = None
        self.update_task_id = None
        self.delete_task_id = None
        self.previous_page = None

    def set_previous_page(self, page_name: str):
        self.previous_page = page_name

    def set_delete_task_id(self, task_id):
        self.delete_task_id = task_id

    def set_access_token(self, token) -> None:
        self.access_token = token

    def get_access_token(self) -> str:
        return self.access_token
