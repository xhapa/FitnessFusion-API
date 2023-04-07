from fastapi import APIRouter, Body, Query, Path
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from services.exercises_log import ExerciseLogService

from sqlmodels.exercises_log import ExerciseLog

from config.database import Session, engine

exercise_route = APIRouter()

@exercise_route.post("/log-exercise")
async def log_exercise(log_data : ExerciseLog = Body()):
    db = Session(engine)
    return ExerciseLogService(db).create_log(log_data)

@exercise_route.get("/users/{user_id}/logs")
async def get_user_logs(user_id: int = Path(...)):
    db = Session(engine)
    logs = ExerciseLogService(db).get_user_logs(user_id)
    if not logs:
        return HTTPException(status_code=404, detail=f"No user logs found for user ID {user_id}")
    return logs

# @app.get("/logs")
# async def get_all_logs() -> List[ExerciseLog]:
#     return log_db.get_all_logs()