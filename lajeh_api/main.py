
from fastapi import FastAPI, APIRouter
from lajeh_api.database import check_connection
from sqlalchemy import create_engine
from lajeh_api.settings import Settings
from lajeh_api.users.controllers import router


engine=create_engine(Settings().DATABASE_URL)


async def setup():
    try:
        check_connection(engine)
        print("Conexão com o banco de dados estabelecida com sucesso.")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")


# Função lifespan
async def lifespan(app):
    await setup()
    yield


# Instância do FastAPI
app = FastAPI(lifespan=lifespan)
app.include_router(router)

