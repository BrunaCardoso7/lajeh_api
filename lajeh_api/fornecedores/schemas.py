import datetime
from pydantic import BaseModel

class FornecedorCreate(BaseModel):
    nome:str
    email:str
    telefone:str
    
class FornecedorResponse(BaseModel):
    id:str
    nome:str
    email:str
    telefone:str
    created_at: datetime
    updated_at:datetime
    
    model_config={
        "from_attributes": True
    }