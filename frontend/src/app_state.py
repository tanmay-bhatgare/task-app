class AppState:
    def __init__(self):
        self.access_token = None
        self.update_task_id = None

    def set_access_token(self, token) -> None:
        self.access_token = token

    def get_access_token(self) -> str:
        return self.access_token
