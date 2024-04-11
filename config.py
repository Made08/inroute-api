import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar datos de configuración desde el archivo JSON
with open('settings.json', 'r') as file:
    config = json.load(file)

# Construir la URL de la base de datos a partir de la configuración
DATABASE_URL = (
    f"postgresql://{config['database']['username']}:{config['database']['password']}@"
    f"{config['database']['host']}:{config['database']['port']}/{config['database']['database']}"
)

# Configurar SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()