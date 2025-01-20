from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from lajeh_api.fornecedores.models import Fornecedor
from lajeh_api.fornecedores.schemas import FornecedorCreate, FornecedorResponse

class Fornecedorrepository:
    def __init__(self, db_session: Session):
        pass