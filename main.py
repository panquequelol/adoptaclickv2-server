from pydantic import BaseModel
from fastapi import FastAPI, Body, Depends, HTTPException
from uuid import uuid4, UUID
from config.database import SessionLocal, engine
from models.index import Base
from schemas.index import UserCreate, UserUpdate, User, PetCreate
from controllers.index import get_user, get_user_by_email, create_user, delete_user, update_user, create_pet, get_pets_by_owner
from sqlalchemy.orm import Session

from routes import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"res": "server is up!"}


# @app.post("/user/")
# def user_create(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db, user_email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return create_user(db, user=user)


# @app.get("/user/")
# def user_get(id: int, db: Session = Depends(get_db)):
#     user = get_user(db, user_id=id)
#     return user


# @app.put("/user/")
# def user_update(updated_user: UserUpdate, db: Session = Depends(get_db)):
#     user = update_user(db, updated_user=updated_user)
#     return user


# @app.delete("/user/")
# def user_delete(id: int, db: Session = Depends(get_db)):
#     res = delete_user(db, user_id=id)
#     return res


@app.post("/pet/")
def pet_create(pet: PetCreate, user_id: int, db: Session = Depends(get_db)):
    res = create_pet(db, pet=pet, user_id=user_id)
    return res


@app.get("/pet/")
def pets_by_owner(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_pets_by_owner(db, owner_id=user_id)
