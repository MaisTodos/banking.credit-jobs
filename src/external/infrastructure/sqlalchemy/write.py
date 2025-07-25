from src.external.infrastructure.sqlalchemy.base import SqlInfrastructure
from src.external.port.infrastructure.sql import ISqlInfrastructureWrite


class SqlAlchemyInfrastructureWrite(SqlInfrastructure, ISqlInfrastructureWrite):
    pass
