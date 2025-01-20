import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()

@table_registry.mapped_as_dataclass
class Fornecedor:
    __tablename__ = "fornecedores"
    
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), server_onupdate=func.now()
    )
    
    nome:Mapped[str] = mapped_column(unique=True, nullable=False)
    email:Mapped[str] = mapped_column(unique=True, nullable=False)
    telefone:Mapped[str] = mapped_column(unique=True, nullable=False)
    
    id:Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)