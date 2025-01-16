from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from lajeh_api.users.models import table_registry  # Certifique-se de que o caminho está correto

# Este é o objeto MetaData que será usado pelo Alembic para autogerar migrações
target_metadata = table_registry.metadata

# Configuração do Alembic
config = context.config

# Configuração do logger com base no arquivo alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    """
    Executa as migrações no modo 'offline'.

    Neste modo, o contexto é configurado com apenas uma URL,
    e não com um Engine. 
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Executa as migrações no modo 'online'.

    Neste modo, um Engine é criado e associado ao contexto.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Verifica se o modo é offline ou online e executa a migração correspondente
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
