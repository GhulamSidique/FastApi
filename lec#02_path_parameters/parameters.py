from fastapi import FastAPI

# initialize the app
app = FastAPI()

# function to get the id with path
@app.get("/blog/{id}") # here every time an id will be displayed in the path
def blog(id):
    # every time we give path like /blog/1 it will display the same id on the screen like blog: "1"
    # here the number will be a str not the int bcz we haven't defined the data type 
    return {"Blog": id}

# function with data type
@app.get("/intblog/{id}")
def intblog(id: int): # id will be an int
    return {"Blog": id}

#===============================================
# this function will not display the return values bcz we have another function above it that if blog
# the above blog function takes unpublished value as an id which is by default a str and will return its value
# so it is necessary to take care of and we have to be very well aware of paths and parameters
@app.get("/blog/unpublished")
def unpublished():
    return "No any unpublished blogs"
#================================================