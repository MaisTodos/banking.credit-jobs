import boto3
from boto3.resources.base import ServiceResource

from src.external.infrastructure.aws.decorator.s3_exception import handle_s3_exception
from src.external.port.infrastructure.aws import IS3BaseInfrastructure


class S3BaseInfrastructure(IS3BaseInfrastructure):
    @handle_s3_exception
    def __init__(self):
        self.__resource = boto3.resource("s3")

    @property
    def resource(self) -> ServiceResource:
        return self.__resource
