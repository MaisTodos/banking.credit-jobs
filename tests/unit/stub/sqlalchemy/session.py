from sqlalchemy import Executable

from tests.unit.stub.sqlalchemy.result import SqlAlchemyStubAsyncResult


class SqlAlchemyStubAsyncSession:
    def __init__(self):
        self.closed_connections = 0
        self.rollbacks_called = 0
        self.executes_called = 0
        self.commits_called = 0
        self.add_called = 0
        self.updates_called = 0
        self.merges_called = 0

    async def scalars(
        self,
        statement: Executable,
        parameters=None,
    ) -> SqlAlchemyStubAsyncResult:
        return SqlAlchemyStubAsyncResult()

    def add(self, instance: object, _warn: bool = True):
        self.add_called += 1

    async def commit(self):
        self.commits_called += 1

    async def close(self):
        self.closed_connections += 1

    async def rollback(self):
        self.rollbacks_called += 1

    async def execute(self, statement, params=None):
        self.executes_called += 1

    async def update(self, instance: object, _warn: bool = True):
        self.updates_called += 1

    async def merge(self, instance: object, _warn: bool = True):
        self.merges_called += 1
