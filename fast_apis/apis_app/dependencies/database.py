from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://sadath:sadath777@16.171.47.42:5432/orm_manage"


engine = create_engine(DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()