from lajeh_api.users.schemas import UserCreate, UserResponse
from lajeh_api.users.services import UserService

class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self, user: UserCreate) -> UserResponse:
        """
        Lógica para criar um novo usuário.
        """
        return self.user_service.create_user(user)