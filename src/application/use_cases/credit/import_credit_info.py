from pathlib import Path

from src.application.port.use_case.credit.import_credit_info import (
    IImportCreditInfoUseCase,
)


class ImportCreditInfoUseCase(IImportCreditInfoUseCase):
    def __init__(self):
        pass

    def __fetch_credit_info(self):
        with Path.open("./src/mock_dados.txt", "r") as credit_data:
            import csv

            csv_dict = csv.DictReader(credit_data)
            return [line for line in csv_dict]

    def perform(self):
        data = self.__fetch_credit_info()
        return data
