from fastapi import APIRouter, FastAPI, UploadFile
from lajeh_api.fornecedores.services import FornecedoresService

app = FastAPI()

router = APIRouter(prefix="/fornecedor", tags=["fornecedor"]) 

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    response = await FornecedoresService.create_upload_fornecedor_service(file)
    return response

# @router.get("/processfile/")
# def process_file (url:str):
#     try:
#         response = FornecedoresService.process_excel_file(url)
#         return response
#     except:
#         print('An exception occurred')