from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho do banco SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Conexão com o banco, com check_same_thread=False para SQLite + FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criar sessão local (SessionLocal = instância de sessão)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base usada pelos modelos
Base = declarative_base()

# Dependency do FastAPI para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
