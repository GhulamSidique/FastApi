# When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
# A request body is data sent by the client to your API. A response body is the data your API sends to the client.
# Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time, sometimes they only request a path, maybe with some query parameters, but don't send a body.
# To declare a request body, you use Pydantic models with all their power and benefits.

from fastapi import FastAPI
from typing import Optional # for creating an optionaal field
from pydantic import BaseModel # used to request the data

app = FastAPI()

# create a class or say block that will have some parameters for the request
# here class will contain the base model from pydantic
class Blog(BaseModel):
    # create a block for the request
    title: str
    body: str
    published: Optional[bool] # this field is an optional with bool dtype


# after creating body or block pass it as a parameter in the function below
@app.post("/blog")
def create(blog: Blog): # here we can also write request in stead of blog
    return f"You have created a blog with {blog.title}"
# to see the results just open swagger ui by /docs and then try it and execute it to see the results
