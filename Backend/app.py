from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    age : int
    id: int 

user = User(name="Rishabh", age=20, id = 1)

# @app.post("/")
# async def users(user: User):
#     return {"user": user}


@app.get("/products")
async def read_products():
    return {"Hello": "World"}

@app.get("/products/{product_id}")
async def read_item(product_id: int, item: str = None):
    return {"product_id": product_id, "item": item} 

