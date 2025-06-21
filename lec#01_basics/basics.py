from fastapi import FastAPI

# initialize the the application
app = FastAPI()


# function to display the message
# there is no restrictions on the name of the function but we have to take care of the path inside the get function
# before function we have to have get the path using app decorator
# to run the script --> open the terminal and go into the folder where code is present and type ==> uvicorn file)name:app --reload
@app.get("/") # here no path is given after /
def index():
    # always return something to display
    return "hello this  message is from fast api"

# get the about page and here the path is /about 
@app.get("/about")
def about():
    return {"about": "this is the about page"}

# get the number
