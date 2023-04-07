from fastapi import APIRouter, Body

from services.user_profile import UserProfileService
from sqlmodels.user_profile import UserProfile

from config.database import Session, engine

user_route = APIRouter()

@user_route.post("/users")
async def create_user_profile(profile_data : UserProfile = Body()):
    db = Session(engine)
    return UserProfileService(db).create_user_profile(profile_data)

# @app.get("/users/{user_id}")
# async def get_user_profile(user_id: int) -> UserProfile:
#     profile = user_db.get_user_profile(user_id)
#     if profile is None:
#         raise HTTPException(status_code=404, detail=f"No user profile found for user ID {user_id}")
#     return profile

# @app.put("/users/{user_id}")
# async def update_user_profile(user_id: int, profile_data: Dict) -> UserProfile:
#     return user_db.update_user_profile(user_id, profile_data)

# @app.delete("/users/{user_id}")
# async def delete_user_profile(user_id: int) -> None:
#     user_db.delete_user_profile(user_id)

# @app.get("/users")
# async def get_all_user_profiles() -> List[UserProfile]:
#     return user_db.get_all_user_profiles()