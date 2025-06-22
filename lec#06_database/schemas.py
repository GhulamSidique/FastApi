from pydantic import BaseModel

class Blog(BaseModel):
    name: str
    designation:str
# create a basse model that will return the values in the database