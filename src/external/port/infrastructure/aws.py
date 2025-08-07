from abc import ABC, abstractmethod
from io import BytesIO


class IS3BaseInfrastructure(ABC):
    pass


class IS3DownloadInfrastructure(IS3BaseInfrastructure, ABC):
    @abstractmethod
    def download_file(self) -> BytesIO:
        pass
