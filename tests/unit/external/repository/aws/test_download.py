from io import BytesIO

import pytest
from botocore.exceptions import ClientError
from moto import mock_aws

from src.external.error import InfrastructureException
from src.external.repository.aws.download import S3BaseDownloadInfrastructure
from src.external.setting.environment import env


@mock_aws
def test_download_parquet_successful():
    infra = S3BaseDownloadInfrastructure()
    bucket_name = env.AWS_S3_BUCKET_NAME
    bucket_path = infra._S3BaseDownloadInfrastructure__build_bucket_key(bucket_name)
    bucket = infra.resource.create_bucket(Bucket=bucket_name)

    obj = infra.resource.Object(bucket.name, bucket_path)
    with open("tests/unit/test_data/good_data.parquet", "rb") as content:
        test_content = content.read()

        obj.put(Body=test_content)

    downloaded_file = infra.download_file()
    assert isinstance(downloaded_file, BytesIO)
    assert downloaded_file.getbuffer().nbytes == 3434


@mock_aws
def test_download_parquet_not_found():
    infra = S3BaseDownloadInfrastructure()
    bucket_name = env.AWS_S3_BUCKET_NAME
    bucket_path = "bad_path"
    bucket = infra.resource.create_bucket(Bucket=bucket_name)

    obj = infra.resource.Object(bucket.name, bucket_path)
    with open("tests/unit/test_data/good_data.parquet", "rb") as content:
        test_content = content.read()

        obj.put(Body=test_content)

        with pytest.raises(InfrastructureException) as error:
            _ = infra.download_file()
        assert error.typename == "InfrastructureException"
        assert isinstance(error.value.original_error, ClientError)
        assert (
            error.value.tag
            == "external.infrastructure.aws.decorator.s3_exception.boto_core_client_error"
        )
