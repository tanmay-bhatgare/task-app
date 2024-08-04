import os


class Paths:
    current_dir = os.getcwd()
    assets_path = os.path.abspath(os.path.join(current_dir, "frontend\\assets"))