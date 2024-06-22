from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, Sessionlocal
from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

models.Base.metadata.create_all(bind=engine)

class AnyBase(BaseModel):
    content : str

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/add", status_code=status.HTTP_201_CREATED)
async def create_any(anything:AnyBase, db:db_dependency):
    db_any = models.Any(**anything.dict())
    db.add(db_any)
    db.commit()

@app.get("/get", status_code=status.HTTP_200_OK)
async def read_any(db:db_dependency):
    anything = db.query(models.Any).order_by(desc(models.Any.id)).first()
    if anything is None:
        raise HTTPException(status_code=404, detail='There is nothing')
    return anything