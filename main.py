from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import create_db_and_tables

from routers.user_profile import user_route
from routers.exercise_log import exercise_route

app = FastAPI()

app.title = 'FitnessFusion API'
app.version = '0.0.1'

app.include_router(user_route)
app.include_router(exercise_route)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get('/')
async def home():
    return HTMLResponse('<h1>FitnessFusion API</h1>') 