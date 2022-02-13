from fastapi import FastAPI

from controller import get_developer

app = FastAPI()


@app.get("/developer/")
async def root(app_id: str):
    return {"developer": get_developer(app_id)}
