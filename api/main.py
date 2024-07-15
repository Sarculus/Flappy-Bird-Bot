from fastapi import FastAPI, HTTPException
from domain_input import TestClass

app = FastAPI()
#http://127.0.0.1:8000/docs#/

items = ["apple", "melon"]
@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/testclass")
def get_testclass():
    p1 = TestClass()
    return p1.test_list

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not found")