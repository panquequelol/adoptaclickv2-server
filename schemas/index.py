from pydantic import BaseModel


class PetBase(BaseModel):
    name: str | None = None
    animal_type: str
    description: str
    price: float | None = None


class PetCreate(PetBase):
    pass


class PetUpdate(PetBase):
    id: int


class Pet(PetBase):
    id: int
    owner_id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    phone_number: str


class UserCreate(UserBase):
    hashed_password: str


class UserUpdate(UserCreate):
    id: int


class User(UserBase):
    id: int
    pets: list[Pet] = []

    class Config:
        orm_mode = True
