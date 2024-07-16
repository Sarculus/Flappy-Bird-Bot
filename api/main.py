from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from domain_input import TestClass

#http://127.0.0.1:8000/docs#/
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["http://localhost:5173/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


items = ["apple", "melon"]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/api")
def root():
    p1 = TestClass()
    return p1.test_list_1
    #return {"Hello": "World"}

@app.get("/api/testclass")
def get_testclass():
    p1 = TestClass()
    return p1.test_list_2

@app.post("/api/items")
def create_item(item: str):
    items.append(item)
    return items

@app.post("/api/start_game_bot")
def start_game_bot():
    print("game bot started")

@app.get("/api/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not found")