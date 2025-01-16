from pydantic import BaseModel
from datetime import datetime
from lajeh_api.users.models import RoleUser


class UserCreate(BaseModel):
    username:str
    email: str
    password:str
    role: RoleUser

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    role: RoleUser
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
