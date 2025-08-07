from freezegun import freeze_time

from src.application.use_cases.credit.import_credit_info import ImportCreditInfoUseCase
from src.domain.entity.credit import BusinessCreditEntity


@freeze_time("2025-07-01")
def test_import_credit_info_success(mocker):
    mocker.patch(
        "src.external.repository.aws.download.S3BaseDownloadInfrastructure.download_file",
        return_value="tests/unit/test_data/good_data.parquet",
    )

    result = ImportCreditInfoUseCase().perform()

    assert len(result) == 5
    assert all([isinstance(el, BusinessCreditEntity) for el in result])


def est_get_credit_info_string_documents(mocker):
    mocker.patch(
        "src.external.repository.aws.download.S3BaseDownloadInfrastructure.download_file",
        return_value="tests/unit/test_data/str_document_data.parquet",
    )

    result = ImportCreditInfoUseCase().perform()

    assert len(result) == 5
    assert all([isinstance(el, BusinessCreditEntity) for el in result])
