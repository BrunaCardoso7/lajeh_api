from pydantic import BaseModel, ConfigDict, computed_field
from datetime import datetime
from lajeh_api.users.models import RoleUser
from sqlalchemy.dialects.postgresql import UUID


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
    
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        json_encoders={
            UUID: str
        }
    )