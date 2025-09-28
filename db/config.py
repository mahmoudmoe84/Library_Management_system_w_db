from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DB_HOST :str
    DB_USER :str
    DB_PASSWORD :str
    DB_DATABASE :str
    DB_PORT : int
    
    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "setting.env")
        env_file_encoding = "utf-8"
        
settings = Settings()