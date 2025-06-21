# swagger ui an open-source tool that provides a visual interface to interact with and test APIs defined using the OpenAPI Specification
# whatever we have created using get request will be displayed on the screen and we can easily visualize them
# for this we have to run the path as /docs after creating our functions for our apis

from fastapi import FastAPI

app = FastAPI()

@app.get("/blog/unpublished")
def unpublished():
    return "No any unpublished blogs"

@app.get("/blog/{id}")
def intblog(id: int): # id will be an int
    return {"Blog": id}

# these two routes will be displayed on the screen when we run /docs as path in the web browser
# we can also clikc on any get route there and click on the "try it on" to check that every thing is performing well
# like we have an intblog function that takes int as parameter but if we check it and insert str in stead it will not run and generate the following message
# Please correct the following validation errors and try again.
# For 'id': Value must be an integer. 