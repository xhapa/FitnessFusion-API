from typing import Optional

from sqlmodels.user_profile import UserProfile
from sqlmodels.exercises_log import ExerciseLog

from fastapi import HTTPException

class ExerciseLogService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_user_logs(self, user_id: int):
        return self.db.query(ExerciseLog).filter(user_id == user_id).all()

    def create_log(self, log_data):
        log = ExerciseLog(**log_data.dict())
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log

    # def get_all_logs(self) -> List[ExerciseLog]:
    #     return list(self.logs.values())