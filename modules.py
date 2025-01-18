import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "lajeh_api")

DEFAULT_FILES = [
    "__init__.py",
    "controllers.py",
    "models.py",
    "schemas.py",
    "repositories.py",
    "routes.py",
    "services.py",
]

def create_modules():
    """
    Cria um novo módulo com arquivos padronizados.
    """
    module_name = input("Nome do módulo: ")
    
    module_path = os.path.join(MODULES_DIR, module_name)
    
    if os.path.exists(module_path):
        print(f"Erro: o módulo {module_name} já existe!")
        return
    
    os.makedirs(module_path)
    print(f"Módulo {module_name} criado com sucesso.")
    
    # Criar arquivos padrões
    for file in DEFAULT_FILES:
        file_path = os.path.join(module_path, file)
        if "/" in file:
            sub_dir = os.path.dirname(file_path)
            os.makedirs(sub_dir, exist_ok=True)
        with open(file_path, "w") as f:
            if file == "__init__.py":
                f.write("# Inicialização do módulo")
            print(f"Arquivo {file} criado em {file_path}")
    
    # Criar a pasta de migrações e inicializar o Alembic
    alembic_dir = os.path.join(module_path, "migrations")
    
    if not os.path.exists(alembic_dir):
        os.makedirs(alembic_dir)
        subprocess.run(["alembic", "init", alembic_dir], check=True)
        print(f"Estrutura de migrações criada em: {alembic_dir}")

# Chama a função
create_modules()
