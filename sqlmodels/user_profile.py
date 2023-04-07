from sqlmodel import SQLModel, Field, Relationship

from datetime import date
from typing import Optional, List

class UserProfile(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    email: str = Field(index=True)
    date_of_birth: date = Field(index=True)
    gender: str = Field(index=True)
    height_cm: int = Field(index=True)
    weight_kg: float = Field(index=True)