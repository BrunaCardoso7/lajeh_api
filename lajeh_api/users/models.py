from enum import Enum
from sqlalchemy.orm import Mapped, registry, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy import func
import uuid

table_registry = registry()

class RoleUser(str, Enum):
    admin = "admin"
    user = "user"

# Mapeamento do objeto relacional
@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"
    
    # Campos com valores padrão devem vir depois
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), server_onupdate=func.now()
    )
    
    # Campos sem valor padrão podem vir antes
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[RoleUser] = mapped_column(nullable=False)
    
    # Agora, o campo 'id' está por último, após os campos com valores padrão
    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
