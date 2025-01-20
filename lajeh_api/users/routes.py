from fastapi import APIRouter, Depends
from lajeh_api.users.schemas import UserCreate, UserResponse
from lajeh_api.users.services import UserService
from lajeh_api.users.dependencies import get_user_service
from lajeh_api.users.controllers import UserController

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserResponse)
async def register_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    user_controller = UserController(user_service=user_service)

    return await user_controller.create_user(user)