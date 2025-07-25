from witch_doctor import WitchDoctor


class DomainException(Exception):
    @WitchDoctor.injection
    def __init__(
        self,
        tag: str,
        details: dict | None = None,
        original_error: Exception | None = None,
    ):
        super().__init__(tag)
        self.tag = tag
        if details is None:
            details = {}
        self.details = details
        self.original_error = original_error
