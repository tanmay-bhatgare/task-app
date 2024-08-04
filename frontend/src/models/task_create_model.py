from datetime import datetime
from typing import Union
from pydantic import BaseModel


class TaskCreateModel(BaseModel):
    title: str
    description: str
    is_private: bool
    due_date: Union[datetime, str]
