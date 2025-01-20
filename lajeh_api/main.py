
from fastapi import FastAPI
from lajeh_api.database import check_connection
from lajeh_api.users.routes import router as user_router
from lajeh_api.fornecedores.controllers import router as fornecedor_router
from lajeh_api.configs.cloudinary.main import configure_cloudinary



async def setup():
    try:
        await check_connection()
        print("Conexão com o banco de dados estabelecida com sucesso.")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")


async def lifespan(app):
    await setup()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(fornecedor_router)

configure_cloudinary()