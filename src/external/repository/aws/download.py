import datetime
from io import BytesIO
from logging import getLogger

from src.external.infrastructure.aws.decorator.s3_exception import handle_s3_exception
from src.external.infrastructure.aws.s3 import S3BaseInfrastructure
from src.external.port.infrastructure.aws import IS3DownloadInfrastructure
from src.external.setting.environment import env

logger = getLogger("external.repository.aws")


class S3BaseDownloadInfrastructure(S3BaseInfrastructure, IS3DownloadInfrastructure):
    def __init__(self):
        super().__init__()
        self.__now = datetime.datetime.now(tz=datetime.UTC)

    def __build_bucket_key(self, bucket) -> str:
        filename = f"{self.__now.year}-{self.__now.month}-{self.__now.day}"
        return f"{bucket}/{filename}"

    @handle_s3_exception
    def download_file(self) -> BytesIO:
        bucket = env.AWS_S3_BUCKET_NAME
        key = self.__build_bucket_key(bucket)

        parquet_buffer = BytesIO()

        s3_object = self.resource.Object(bucket, key)
        s3_object.download_fileobj(parquet_buffer)

        parquet_buffer.seek(0)

        return parquet_buffer
