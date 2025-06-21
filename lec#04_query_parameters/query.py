# query parameters are used to limit the values sto be displayed 
# The query string parameter is defined after the question mark (?) in the endpoint's query string.
# using query parameters we can reduce the number of endpoints required for an API. Instead of creating separate endpoints for each filtering option, a single endpoint can handle multiple query parameters.
# they are used like /blog?limit=20

from fastapi import FastAPI
app = FastAPI()

@app.get("/blog")
def index(limit):
    # we have to search like --> http://127.0.0.1:8000/blog?limit=20
    return {"Blogs": f"we have {limit} blogs"}

# we can also set a limit like if we do not provide any number in limit then default value will be displayed
@app.get("/defaultblog")
def index(limit = 10): #by default 10
    # we have to search like --> http://127.0.0.1:8000/defaultblog
    # if limit value is forgoten then by default 10 will be dispayed
    return {"default Blogs": f"we have {limit} blogs"}