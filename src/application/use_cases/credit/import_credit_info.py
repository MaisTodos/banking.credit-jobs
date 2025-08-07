import uuid
from collections import defaultdict
from datetime import datetime
from logging import getLogger

import polars
from witch_doctor import WitchDoctor

from src.application.port.use_case.credit.import_credit_info import (
    IImportCreditInfoUseCase,
)
from src.domain.entity.credit import BusinessCreditEntity
from src.domain.error.error import DomainException
from src.external.port.infrastructure.aws import IS3DownloadInfrastructure

CONVERT_FROM_PARQUET = {
    "lmt_arv": "cgr",
    "lmt_slr": "qia",
}

logger = getLogger("application.use_cases.credit")


class ImportCreditInfoUseCase(IImportCreditInfoUseCase):
    @WitchDoctor.injection
    def __init__(self, download_infrastructure: IS3DownloadInfrastructure):
        self.__download_infrastructure = download_infrastructure

    def __fetch_credit_info(self) -> polars.LazyFrame:
        credits_file = self.__download_infrastructure.download_file()
        credits_file_data = polars.scan_parquet(credits_file)
        return credits_file_data

    def __get_credit_info_from_raw(
        self, credits_file: polars.LazyFrame
    ) -> polars.DataFrame:
        required_columns = ("cnpj_num", "produto", "lmt_max")
        current_date = datetime.today().date()
        return (
            credits_file.filter(polars.col("dt_mes_ref").dt.date() == current_date)
            .filter(polars.col("cnpj_num") is not None)
            .filter(polars.col("lmt_max") is not None)
            .sort("dt_mes_ref")
            .select(*required_columns)
            .collect()
        )

    def __group_raw_info_by_document(self, raw_info: polars.DataFrame) -> list:
        raw_credit_info = defaultdict(lambda: {"cgr": 0, "qia": 0})
        for row in raw_info.rows():
            has_key_and_value = (
                row[0] is not None and row[1] is not None and row[2] is not None
            )
            if has_key_and_value:
                raw_credit_info[row[0]][CONVERT_FROM_PARQUET[row[1]]] = row[2]
        return raw_credit_info

    def __validate_downloaded_data(self, unvalidated_info: list) -> list:
        validated_info = []
        for document in unvalidated_info:
            try:
                validated_business = BusinessCreditEntity.create(
                    id=uuid.uuid4(),
                    document=document,
                    cgr=unvalidated_info[document]["cgr"],
                    qia=unvalidated_info[document]["qia"],
                )
                validated_info.append(validated_business)
            except DomainException as error:
                details = {
                    "original_error": error.original_error,
                    "tag": error.tag,
                    "original_details": error.details,
                }
                logger.error(
                    f"Error while validating business credit data {document}",
                    extra=details,
                )

        return validated_info

    def perform(self) -> list:
        raw_data = self.__fetch_credit_info()
        raw_credit_data = self.__get_credit_info_from_raw(raw_data)
        grouped_credit_info = self.__group_raw_info_by_document(raw_credit_data)
        validated_data = self.__validate_downloaded_data(grouped_credit_info)
        return validated_data
