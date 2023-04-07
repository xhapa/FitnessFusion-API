from sqlmodel import SQLModel, Field

from datetime import date

class UserProfile(SQLModel, table=True):
    user_id: int = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    email: str = Field(index=True)
    date_of_birth: date = Field(index=True)
    gender: str = Field(index=True)
    height_cm: int = Field(index=True)
    weight_kg: float = Field(index=True)