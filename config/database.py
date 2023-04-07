from sqlmodel import Session, SQLModel, create_engine
from sqlmodels.exercises_log import ExerciseLog
from sqlmodels.user_profile import UserProfile

sqlite_file_name = "db.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)