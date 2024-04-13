""" Sets the app configuration from enviroment variables """
import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    """ A settings class that sets all variables """
    PROJECT_NAME:str = "Database project"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT : int = 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","test")

    DATABASE_URL = f"postgresql://pythonbasecourse_user:RHudAM9bTVZWN4MHLwMXCmaGNB8AyU6h@dpg-co4pcpi1hbls73c04tug-a.oregon-postgres.render.com/pythonbasecourse"
    
    #f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"



settings = Settings()