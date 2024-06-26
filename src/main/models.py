from pydantic_settings import BaseSettings
# from typing import List

"""
Configuration class for the app.
Precendences:
1. ENV Vars
2. .env File
3. Default Vars
"""

class AppSettings(BaseSettings):
    api_port: int | None = 8000
    custom_message: str | None = "Here could be your message"

    class Config:
        env_file = ".env"