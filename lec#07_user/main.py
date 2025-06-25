# now get the user data
from fastapi import FastAPI, Depends, HTTPException, Response, status
import models, schemas
from sqlalchemy.orm import Session
from db_connection import engine, session
from passlib.context import CryptContext # to hash the password

app = FastAPI()

# get the base from the models
models.base.metadata.create_all(engine)

# get the db
def load_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# bycrypt the password
bycrypted = CryptContext(schemes=['bcrypt'], deprecated ="auto")

# create the user
@app.post("/user", status_code = status.HTTP_201_CREATED)
def user(request:schemas.User, db: Session = Depends(load_db)):
    # hash the passowrd
    hashed_pass = bycrypted.hash(request.password)
    new_user = models.User(name = request.name, email = request.email, password = hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get the user
@app.get("/user/{id}", status_code=status.HTTP_200_OK, response_model=schemas.showUser)
def get_user(id, response:Response, db:Session = Depends(load_db)):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'Blog of id {id} not found in db')
    
    return users

# update the user by id
@app.put("/user/{id}", status_code=status.HTTP_200_OK)
def update(id, request:schemas.User, db:Session=Depends(load_db)):
    updated = db.query(models.User).filter(models.User.id == id)
    if not updated.first():
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user of id {id} not in db")
    # Hash the password before update 
    hashed_pass = bycrypted.hash(request.password)
    # update the required things
    updated.update({"name": request.name,"email": request.email,"password": hashed_pass})
    db.commit()
    return "update_user"