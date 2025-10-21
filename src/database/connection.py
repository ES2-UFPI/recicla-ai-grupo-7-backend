from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from contextlib import contextmanager
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não está configurada no .env")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Importa Base dos models
from src.models.models import Base


def create_database():
    """Cria todas as tabelas no banco de dados"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created!")


@contextmanager
def get_db():
    """
    Context manager para obter sessão do banco.
    
    Uso:
        with get_db() as db:
            users = db.query(User).all()
            # db fecha automaticamente ao sair do bloco
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()