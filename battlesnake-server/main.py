from fastapi import FastAPI, Request
from load_model import load_model, choose_move

app = FastAPI()
model = load_model("snake_model.zip")

@app.get("/")
def read_root():
    return {"message": "Battlesnake is alive!"}

@app.post("/move")
async def move(request: Request):
    game_state = await request.json()
    move = choose_move(game_state, model)
    return {"move": move}

@app.post("/start")
def start():
    return {"color": "#00FF00", "headType": "default", "tailType": "default"}

@app.post("/end")
def end():
    return {}

