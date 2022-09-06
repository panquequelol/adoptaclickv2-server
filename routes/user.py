from fastapi import Depends, HTTPException, APIRouter
from schemas.index import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from controllers.index import get_user, get_user_by_email, create_user, delete_user, update_user
from config.database import get_db

router = APIRouter(prefix="/user",  tags=["user"])


@router.post("/")
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user_email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user=user)


@router.get("/")
def user_get(id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id=id)


@router.put("/")
def user_update(updated_user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, updated_user=updated_user)


@router.delete("/")
def user_delete(id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id=id)
