from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    age : int
    id: int 

user = User(name="Rishabh", age=20, id = 1)

@app.get("/")
async def users(user: User):
    return {"user": user}


@app.get("/root")
async def read_root():
    return {"Hello": "World"}


@app.get("/home")
async def read_home():
    return {"Hello": "Home"}