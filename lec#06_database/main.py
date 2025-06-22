from fastapi import FastAPI, Depends, status, Response, HTTPException
import models, schemas
from database import engine, session
from sqlalchemy.orm import Session

app = FastAPI()

models.base.metadata.create_all(engine)

# load the database
def load_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# create the post request
# whenever we create a blog the status code must be 201
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_db(request: schemas.Blog, db:Session=Depends(load_db)):
    # create the model here
    new_model = models.blog(name=request.name, designation= request.designation)
    # add the model in db
    db.add(new_model)
    # commit it
    db.commit()
    # refresh
    db.refresh(new_model)
    return new_model

# fucntion to get or display all db valaues 
@app.get("/blog", status_code=status.HTTP_200_OK)
def get_db(db: Session=Depends(load_db)):
    blogs = db.query(models.blog).all() # .all will return all values
    return blogs

# function to get the blog by giving an id
# check it by /docs and click try it on of the blog/{id} get method
@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def by_id(id, response: Response ,db:Session = Depends(load_db)):
    blog_by_id = db.query(models.blog).filter(models.blog.id==id).first() # will return the first value by id
    if not blog_by_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog of id {id} not found in the db")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Sttus": f"Blog of id {id} not found in the db"}
    return blog_by_id

# function to delete a blog
@app.delete("/blog", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session=Depends(load_db)):
    db.query(models.blog).filter(models.blog.id==id).delete(synchronize_session=False)
    db.commit()
    return f"deleted blog of id {id}"