from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.db_uri

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db_session() -> Generator[Session, None, None]:
    """Get a database session"""
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


def get_db_engine() -> Engine:
    """Get a database engine"""
    return engine
