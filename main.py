from fastapi import FastAPI
from config.database import engine
from models.index import Base

from routes import user, pet

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(pet.router)


@app.get("/")
def home():
    return {"res": "server is up!"}
