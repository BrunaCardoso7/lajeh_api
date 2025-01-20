from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from sqlalchemy.exc import SQLAlchemyError
from lajeh_api.users.models import User
from lajeh_api.users.schemas import UserCreate, UserResponse
from uuid import uuid4

class UserRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_user_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self.db_session.execute(stmt)
        return result.scalars().first()

    async def create_user_rp(self, user: UserCreate) -> UserResponse:
        try:
            user_data = user.model_dump()  
            user_data['id'] = str(uuid4())  

            new_user = User(**user_data)

            self.db_session.add(new_user)
            await self.db_session.commit()
            await self.db_session.refresh(new_user)
            
            return UserResponse.model_validate({
                'id': str(new_user.id),  
                'username': new_user.username,
                'email': new_user.email,
                'role': new_user.role,
                'updated_at': new_user.updated_at,
                'created_at': new_user.created_at
            })
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            raise ValueError(f"Erro ao criar o usuário: {str(e)}")
