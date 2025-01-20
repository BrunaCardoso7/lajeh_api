from fastapi import Depends
from sqlalchemy.orm import Session
from lajeh_api.database import get_db
from lajeh_api.users.repositories import UserRepository
from lajeh_api.users.services import UserService
# from lajeh_api.users.controllers import UserController

def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db_session=db)

def get_user_service(user_repository: UserRepository = Depends(get_user_repository)):
    return UserService(user_repository=user_repository)

# def get_user_controller(user_service: UserService = Depends(get_user_service)):
#     return UserController(user_service=user_service)