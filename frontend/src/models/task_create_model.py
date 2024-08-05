from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel


class TaskCreateModel(BaseModel):
    title: str
    description: str
    is_private: bool
    due_date: Optional[Union[datetime, str]] = None
