from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# path to the db
db_path = "sqlite:///./my_db.db"

# engine
engine = create_engine(db_path, connect_args={"check_same_thread": False})

# session
session = sessionmaker(bind=engine, autoflush=False, autocommit = False)

# base
base = declarative_base()