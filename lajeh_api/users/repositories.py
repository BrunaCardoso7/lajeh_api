from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from lajeh_api.users.models import User
from lajeh_api.users.schemas import UserCreate, UserResponse
from uuid import uuid4

class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_user_by_username(self, username: str) -> User | None:
        """
        Busca um usuário pelo nome de usuário.
        """
        return self.db_session.query(User).filter(User.username == username).first()

    def create_user_rp(self, user: UserCreate) -> UserResponse:
        """
        Cria um novo usuário no banco de dados.
        """
        existing_user = self.db_session.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise ValueError(f"Email {user.email} já está em uso.")
        try:
            user_data = user.model_dump()
            user_data['id'] = uuid4() 
            # Criando a instância do usuário
            new_user = User(**user_data)
            # Salvando no banco de dados
            self.db_session.add(new_user)
            self.db_session.commit()
            self.db_session.refresh(new_user)

            # Convertendo para o esquema de resposta usando `model_validate`
            return {**vars(new_user), 'id': str(new_user.id)} 
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise ValueError(f"Erro ao criar o usuário: {str(e)}")
