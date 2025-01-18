import cloudinary.uploader
import requests
# import pandas as pd

from fastapi import UploadFile
from io import BytesIO
from fastapi import UploadFile

class FornecedoresService:
    @staticmethod
    async def create_upload_fornecedor_service(file: UploadFile):
        try:
            file_byte = await file.read()
            
            uploud_result = cloudinary.uploader.upload(
                file=file_byte, 
                resource_type="auto",
                public_id=file.filename.split(".")[0] 
            )
            
            return {"secure_url": uploud_result["secure_url"]}

        except:
            print('An exception occurred')
            