from fastapi import Depends, HTTPException, APIRouter
from schemas.index import PetCreate
from sqlalchemy.orm import Session
from controllers.index import create_pet, get_pets_by_owner
from config.database import get_db

router = APIRouter(prefix="/pet",  tags=["pet"])


@router.post("/")
def pet_create(pet: PetCreate, user_id: int, db: Session = Depends(get_db)):
    return create_pet(db, pet=pet, user_id=user_id)


@router.get("/")
def pets_by_owner(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_pets_by_owner(db, owner_id=user_id)
