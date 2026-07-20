#create_engine = creates a connection between our application and postgresql.
from sqlalchemy import create_engine
#declarative_base = is a function that returns a new base class from which all mapped classes should inherit.
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    #Creates a brand-new database session.
    db = SessionLocal()

    try:
        yield db

    finally:
        #After the endpoint finishes, the session is always closed , Even if an exception occurs.
        db.close()