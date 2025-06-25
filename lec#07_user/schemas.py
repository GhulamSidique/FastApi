# create the schema that will be displayed to the user on the screen
from pydantic import BaseModel

# base model
class User(BaseModel):
    name: str
    email: str
    password: str

# a class that will only display the name and the email but not the id
class showUser(BaseModel):
    name: str
    email: str
    # password: str

    # clas that will avoid displaying the id
    class Config():
        orm_mode = True
