from database import base
from sqlalchemy import Column, Integer, String

# craete a class that will extend the base of database file
class blog(base):
    # name of the table
    __tablename__  = "My data"

    # adding columns to the table
    # primary key
    id = Column(Integer, primary_key=True, index=True)
    # title
    name = Column(String)
    designation = Column(String)


