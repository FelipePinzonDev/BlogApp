from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from db import engine, SessionLocale
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str    



def get_db():
    db = SessionLocale()
    try:
        yield db
    finally:
        db.close()    

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase, db:db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()