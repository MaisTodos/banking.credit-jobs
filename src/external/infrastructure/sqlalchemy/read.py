from src.external.infrastructure.sqlalchemy.base import SqlInfrastructure
from src.external.port.infrastructure.sql import ISqlInfrastructureRead


class SqlAlchemyInfrastructureRead(SqlInfrastructure, ISqlInfrastructureRead):
    pass
