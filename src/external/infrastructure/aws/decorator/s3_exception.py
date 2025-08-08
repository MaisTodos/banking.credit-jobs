from functools import wraps
from logging import getLogger

import sentry_sdk
from botocore.exceptions import ClientError
from sentry_sdk import push_scope

from src.external.error import InfrastructureException, UnexpectedException

logger = getLogger("external.infrastructure.aws")


def handle_s3_exception(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ClientError as error:
            send_to_sentry(error)
            details = {
                "error_code": error.response["Error"]["Code"],
                "error_message": error.response["Error"]["Message"],
                "response_metadata": error.response["ResponseMetadata"],
            }
            logger.debug(
                "Error client",
                extra={"props": details},
            )
            raise InfrastructureException(
                tag="external.infrastructure.aws.decorator.s3_exception.boto_core_client_error",
                details=details,
                original_error=error,
            ) from error
        except Exception as error:
            send_to_sentry(error)
            logger.exception(
                "handle_s3_exception error when handling error",
                extra={
                    "error": repr(error),
                },
            )
            raise UnexpectedException(
                tag="external.infrastructure.aws.decorator.s3_exception.unexpected_error"
            ) from error  # pylint: disable=W0719

    return wrapper


def send_to_sentry(error):
    with push_scope() as scope:
        if isinstance(error, ClientError):
            scope.set_tag("task_error_tag", "aws.s3.ClientError")
        else:
            scope.set_tag("error_tag", "unexpected_error")

        sentry_sdk.capture_exception(error=error)
