from fastapi import HTTPException, status
from lajeh_api.users.schemas import UserCreate, UserResponse
from lajeh_api.users.repositories import UserRepository
import asyncio

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
    async def create_user(self, user: UserCreate) -> UserResponse:
        existing_user, new_user = await asyncio.gather(self.user_repository.get_user_by_username(user.username), self.user_repository.create_user_rp(user))
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="E-mail já cadastrado!"
            )
            
        
        return UserResponse.model_validate(new_user)