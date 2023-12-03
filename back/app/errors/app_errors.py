from typing import NamedTuple


class ErrorsCodes(NamedTuple):
    """List of error codes"""

    internal: str = "APP_SERVICE_INTERNAL_ERROR"
    bad_request: str = "APP_SERVICE_BAD_REQUEST"


errors_codes = ErrorsCodes()


class AppServiceError(Exception):
    """General exception of the app"""

    def __init__(
        self,
        message: str = "Internal server error",
        error_code: str = errors_codes.internal,
        status_code: int = 500,
    ) -> None:
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        super().__init__(self.message)


class BadRequestError(AppServiceError):
    """Error due to a bad request"""

    def __init__(
        self,
        message: str = "Bad request error",
        error_code: str = errors_codes.bad_request,
        status_code: int = 400,
    ) -> None:
        self.message = f"Bad request: {message}"
        self.error_code = error_code
        self.status_code = status_code
