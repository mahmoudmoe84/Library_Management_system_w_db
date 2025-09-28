from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DB_HOST :str
    DB_USER :str
    DB_PASSWORD :str
    DB_DATABASE :str
    DB_PORT : int
    
    class Config:
        env_file = "setting.env"
        env_file_encoding = "utf-8"
        
settings = Settings()