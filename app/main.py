from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Values(BaseModel):
    value1: str
    value2: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add/")
async def add(values: Values):
    a=int(values.value1)
    b=int(values.value2)
    return {"sum": (a+b)}