from pydantic import BaseModel
from fastapi import FastAPI, Body, Depends, HTTPException
from uuid import uuid4, UUID
from config.database import SessionLocal, engine
from models.index import Base
from schemas.index import UserCreate, UserUpdate, User, PetCreate
from controllers.index import get_user, get_user_by_email, create_user, delete_user, update_user, create_pet, get_pets_by_owner
from sqlalchemy.orm import Session

from routes import user, pet

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(pet.router)


@app.get("/")
def home():
    return {"res": "server is up!"}
