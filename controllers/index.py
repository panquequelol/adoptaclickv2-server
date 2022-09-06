from sqlalchemy.orm import Session
from models.index import User, Pet
from schemas.index import UserCreate, UserUpdate, PetCreate, PetUpdate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()


def create_user(db: Session, user: UserCreate):
    encrypted_password = user.hashed_password + \
        'letssayididencryptthisinsteadofjustaddingthistext'
    db_user = User(name=user.name, email=user.email,
                   hashed_password=encrypted_password, phone=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, updated_user: UserUpdate):
    res = db.query(User).filter(
        User.id == updated_user.id).update({User.email: updated_user.email, User.name: updated_user.name, User.phone: updated_user.phone_number})
    db.commit()
    return res


def delete_user(db: Session, user_id: int):
    user_deleted = db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return user_deleted


def create_pet(db: Session, pet: PetCreate, user_id: int):
    db_pet = Pet(**pet.dict(), owner_id=user_id)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pet).offset(skip).limit(limit).all()


def get_pets_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(Pet).filter(Pet.owner_id == owner_id).offset(skip).limit(limit).all()


def update_pet(db: Session, updated_pet: PetUpdate):
    res = db.query(Pet).filter(Pet.id == updated_pet.id).update(
        {Pet.name: updated_pet.name, Pet.price: updated_pet.price, Pet.animal_type: updated_pet.animal_type, Pet.description: updated_pet.description})
    db.commit()
    return res
