import i18n

from src.external.port.infrastructure.i18n import Ii18nInfrastructure


class PythonI18nInfra(Ii18nInfrastructure):
    def translator(self, key: str) -> str:
        return i18n.t(key)
