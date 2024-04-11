import json
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def load_settings(env: str):
    """Carga la configuración según el ambiente."""
    with open(f"settings.{env}.json", "r") as f:
        return json.load(f)

# Manejo del argumento de línea de comandos
if len(sys.argv) > 1:
    # Verifica que el argumento tenga el formato esperado "--env=desarrollo"
    if sys.argv[1].startswith("--env="):
        # Extrae el valor del ambiente después del "="
        environment = sys.argv[1].split("=")[1]
    else:
        # Si el argumento no tiene el formato esperado, utiliza el valor predeterminado
        print("Advertencia: Argumento de ambiente no proporcionado correctamente. Usando 'dev' por defecto.")
        environment = "dev"
else:
    # Si no se proporciona ningún argumento, usa el valor predeterminado
    environment = "dev"

# Carga la configuración apropiada según el ambiente
settings = load_settings(environment)

# Extrae la configuración de la base de datos
db_config = settings.get("DATABASE", {})
user = db_config.get("user")
password = db_config.get("password")
host = db_config.get("host", "localhost")
port = db_config.get("port", 5432)
db = db_config.get("db")

# Construye la URL de la base de datos
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"

# Crea la conexión a la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Otras configuraciones que puedas necesitar
DEBUG = settings.get("DEBUG", False)
SECRET_KEY = settings.get("SECRET_KEY", "your_default_secret_key")

# Aquí puedes agregar otras configuraciones personalizadas que necesites