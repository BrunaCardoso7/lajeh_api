
# README do Projeto gestao de pedidos Django apiRest


## Descrição
Instruções para configurar o ambiente de desenvolvimento da api de pedidos e executar o projeto em seu sistema.


### Detalhe importante*

Na raiz do projeto está disponível um arquivo de coleção com todas as rota do projeto já pre-definidas para utilização em programas como postman e insomnia:
```bash
./rotas_api_pedidos_postman_insominia.json
```
## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- **Python 3.x**: 
- **poetry**:

### Url para acesso da documentação:

```bash
http://127.0.0.1:8000/api/schema/swagger-ui/#/
```

## Passos para Executar o Projeto

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu computador. Abra o terminal e execute o seguinte comando:

```bash
git clone https://github.com/BrunaCardoso7/lajeh_api.git
```


### 2. Acessar o Diretório do Projeto

Após clonar o repositório, entre no diretório do projeto:

```bash
cd gestao_de_pedidos_Django_apiRest
```

### 4. Instalar as Dependências

Agora que o ambiente virtual está ativado, instale as dependências do projeto usando o pip. Execute:

```bash
poetry install
```

## 4. Instalar as Dependências adicionais

Agora que o ambiente virtual está ativado, instale as dependências do projeto usando o pip. Execute:

```bash
poetry add fastapi sqlalchemy pydantic-settings psycopg2 psycopg2-binary alembic uvicorn

```


### 3. Ativar Ambiente Virtual

- Ativando o ambiente virtual, poetry:
  
```bash
    source $(poetry env info --path)/bin/activate
```



### 7. Executar o Projeto

Após as dependências estarem instaladas, você pode rodar o servidor com o seguinte comando:
```bash
fastapi dev lajeh_api/main.py
```




### 8. Testar o Projeto

execute-os para garantir que tudo esteja funcionando corretamente:

os teste garante que o funcionamento das rotas e requisitos solicitados estejam funcionando

```bash
python manage.py test
```
****