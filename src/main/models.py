from pydantic import BaseModel
from typing import List

class AppConfig(BaseModel):
    """
    This is the configuration Class for the App.
    It uses pydantics BaseModel to declare the Types
    and what happens, when the entry is not defined.
    """
    api_port : int | None = None
    custom_message : str | None = None
