from witch_doctor import WitchDoctor

from src.external.port.infrastructure.i18n import Ii18nInfrastructure


class ApplicationException(Exception):
    @WitchDoctor.injection
    def __init__(
        self,
        tag: str,
        i18n: Ii18nInfrastructure,
        details: dict | None = None,
        original_error: Exception | None = None,
    ):
        super().__init__(tag)
        self.tag = tag
        self.message = i18n.translator(tag)
        if details is None:
            details = {}
        self.details = details
        self.original_error = original_error
