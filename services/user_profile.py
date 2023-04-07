from typing import Optional

from sqlmodels.user_profile import UserProfile

from fastapi import HTTPException

class UserProfileService():
    def __init__(self, db) -> None:
        self.db = db

    def get_user_profile(self, user_id: int) -> Optional[UserProfile]:
        return self.db.get(UserProfile, user_id)

    def create_user_profile(self, profile_data) -> UserProfile:
        profile = UserProfile(**profile_data.dict())
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def update_user_profile(self, user_id: int, profile_data) -> UserProfile:
        profile = self.get_user_profile(user_id)
        if not profile:
            return HTTPException(status_code=404, detail="Profile not found")
        profile_data = profile_data.dict(exclude_unset=True)
        for key, value in profile_data.items():
            setattr(profile, key, value)
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def delete_user_profile(self, user_id: int) -> None:
        profile = self.db.query(UserProfile).filter(user_id == user_id).first()
        self.db.delete(profile)

    def get_all_user_profiles(self):
        return self.db.query(UserProfile).all()