from tests.unit.stub.sqlalchemy.session import SqlAlchemyStubAsyncSession


class SqlAlchemyStubAsyncSessionMaker:
    def __init__(self):
        self.__session = None

    def __call__(self, *args, **kwargs):
        self.__session = SqlAlchemyStubAsyncSession()
        return self.__session
