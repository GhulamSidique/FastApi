# import libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# path of the database to store values
db_path = "sqlite:///./my_db.db"

# first we need to create the engine for our database
# the following code is taken from fastapi documentation for sql
engine= create_engine(db_path, connect_args = {"check_same_thread": False})

# after creating engine we have to create a session
session = sessionmaker(bind=engine, autoflush=False, autocommit = False,) 

# finally create a ddecelartive base
base = declarative_base()