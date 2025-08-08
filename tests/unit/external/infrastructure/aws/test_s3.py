# Test S3 client class S3BaseInfrastructure(IS3BaseInfrastructure):
from unittest.mock import patch

import pytest
from botocore.exceptions import ClientError
from moto import mock_aws

from src.external.infrastructure.aws.s3 import S3BaseInfrastructure


@mock_aws
def test_establish_connection_create_bucket_and_check_exists():
    bucket_name = "bucket42"
    infra = S3BaseInfrastructure()

    bucket = infra.resource.create_bucket(Bucket=bucket_name)

    assert bucket.name == bucket_name

    client = infra.resource.meta.client
    response = client.head_bucket(Bucket=bucket_name)
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200


mock_aws()


def test_resource_invalid_error():
    with patch("botocore.client.BaseClient._make_request") as mock_request:
        mock_request.side_effect = ClientError(
            error_response={
                "Error": {"Code": "TestIssue", "Message": "Generic error message"}
            },
            operation_name="CreateBucket",
        )

        with pytest.raises(ClientError) as exc_info:
            infra = S3BaseInfrastructure()
            infra.resource.create_bucket(Bucket="test-bucket")

        assert exc_info.value.response["Error"]["Code"] == "TestIssue"
