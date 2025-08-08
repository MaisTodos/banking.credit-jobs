from src.external.infrastructure.sqlalchemy.base import SqlInfrastructure


class SqlAlchemyInfrastructure(SqlInfrastructure):
    def __init__(self, connect_args, echo):
        super().__init__(connect_args, echo)
