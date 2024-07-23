from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from domain_test_input import TestClass

# from domain.main.flappy_bird import FlappyBird

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
    # fb = FlappyBird()
    # top_left_x_y_cor = fb.start_game()  # runs only the first time when you start the python script
    # fb.start_gameplay_loop(fb.frame_count, top_left_x_y_cor, fb.pipe_position)

@app.get("/api/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not found")