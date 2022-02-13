from fastapi import FastAPI

from models import *

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("eddae030-dd89-4a58-8f0b-f85cafa87631"),
        first_name="Aissa",
        last_name="Trad",
        gender=Gender.male,
        role=[Role.student],
    ),
    User(
        id=UUID("3ec0e7f9-684d-4d29-98af-12e00819e577"),
        first_name="Siwar",
        last_name="Trad",
        gender=Gender.female,
        role=[Role.admin, Role.student],
    )
]


@app.get("/users")
async def root():
    return db


@app.post("/add")
async def new_user(user: User):
    db.append(user)
    return {"id": user.id}


