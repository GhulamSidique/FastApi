# define the model
from sqlalchemy import Column, String, Integer
from db_connection import base

class User(base):
    __tablename__="User DB"

    # create the columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    