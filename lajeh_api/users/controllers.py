from fastapi import FastAPI,APIRouter, HTTPException, status, Depends
from lajeh_api.users.services import UserService
from lajeh_api.users.schemas import UserCreate, UserResponse
from lajeh_api.users.models import User
from sqlalchemy.orm import Session
from lajeh_api.users.repositories import UserRepository
from lajeh_api.database import get_db

app = FastAPI()
router = APIRouter(prefix="/users", tags=["users"]) 

@router.post("/regisiter", response_model=None)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)
    return repository.create_user_rp(user)