from fastapi import FastAPI
from models import CreateUser



app = FastAPI()


@app.get('/')
async def get_user():
    return {"msg": "hello"}


@app.post("/")
async def create_user():
    return {"msg": "hello"}