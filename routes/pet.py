from fastapi import Depends, HTTPException, APIRouter
from schemas.index import PetCreate, PetUpdate
from sqlalchemy.orm import Session
from controllers.index import create_pet, get_pets_by_owner, update_pet, get_pets
from config.database import get_db

router = APIRouter(prefix="/pet",  tags=["pet"])


@router.post("/")
def pet_create(pet: PetCreate, user_id: int, db: Session = Depends(get_db)):
    return create_pet(db, pet=pet, user_id=user_id)


@router.get("/")
def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_pets(db, skip=skip, limit=limit)


@router.get("/{user_id}")
def pets_by_owner(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_pets_by_owner(db, owner_id=user_id, skip=skip, limit=limit)


@router.put("/")
def pet_update(updated_pet: PetUpdate, db: Session = Depends(get_db)):
    return update_pet(db, updated_pet=updated_pet)
