from fastapi import FastAPI
app = FastAPI()
@app.get("/root")
async def read_root():
    return {"Hello": "World"}


@app.get("/home")
async def read_home():
    return {"Hello": "Home"}