from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from domain.api.domain_test_input import TestClass
from domain.source.flappy_working import FlappyBird

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
    import redis
    r = redis.Redis(
        host='redis-17414.c327.europe-west1-2.gce.redns.redis-cloud.com',
        port=17414,
        password='TZgxGtwgJost678XJpsSKdndjYFBQltA',
        decode_responses=True)

    sorted_list = r.zrange('highscorestest7', 0, 9, desc=True, withscores=True)
    return_list = []
    for i in range(len(sorted_list)):
        score_part = sorted_list[i][1]
        date_part = sorted_list[i][0]
        date_part_split = date_part.split(" ")
        date_score = [date_part_split[1], score_part]
        return_list.append(date_score)
    return return_list

@app.post("/api/items")
def create_item(item: str):
    items.append(item)
    return items

@app.post("/api/start_game_bot")
def start_game_bot():
    print("game bot started")
    fb = FlappyBird()
    top_left_x_y_cor = fb.start_game()
    fb.start_gameplay_loop(fb.frame_count, top_left_x_y_cor, fb.pipe_position, fb.bird_position, fb.old_bird_speed)

@app.post("/api/stop_game_bot")
def start_game_bot():
    print("game bot stopped")

@app.get("/api/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not found")