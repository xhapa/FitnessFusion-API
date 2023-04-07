from typing import Optional, List

from sqlmodel import SQLModel, Field,  Relationship

from .user_profile import UserProfile

from datetime import time

class ExerciseLog(SQLModel, table=True):
    exercise_id : Optional[int] = Field(default = None, primary_key=True)
    name: str = Field(index=True)
    duration: time = Field(index=True)
    calories_burned: Optional[int] = Field(..., index=True)
    weight: float = Field(index=True)
    sets: int  = Field(index=True)
    reps: int  = Field(index=True)
    user_id : Optional[int] = Field(default = None, foreign_key=UserProfile.user_id)

