from typing import Any
from fastapi.exception_handlers import HTTPException

class BadRequestException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=400, detail=detail)

class UnauthorizedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=401, detail=detail)

class PaymentRequiredException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=402, detail=detail)

class ForbiddenException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=403, detail=detail)

class NotFoundException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=404, detail=detail)

class MethodNotAllowedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=405, detail=detail)

class NotAcceptableException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=406, detail=detail)

class ProxyAuthenticationRequiredException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=407, detail=detail)

class RequestTimeoutException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=408, detail=detail)

class ConflictException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=409, detail=detail)

class GoneException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=410, detail=detail)

class LengthRequiredException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=411, detail=detail)

class PreconditionFailedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=412, detail=detail)

class PayloadTooLargeException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=413, detail=detail)

class URITooLongException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=414, detail=detail)

class UnsupportedMediaTypeException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=415, detail=detail)

class RangeNotSatisfiableException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=416, detail=detail)

class ExpectationFailedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=417, detail=detail)

class ImATeapotException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=418, detail=detail)

class MisdirectedRequestException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=421, detail=detail)

class UnprocessableEntityException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=422, detail=detail)

class LockedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=423, detail=detail)

class FailedDependencyException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=424, detail=detail)

class TooEarlyException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=425, detail=detail)

class UpgradeRequiredException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=426, detail=detail)

class PreconditionRequiredException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=428, detail=detail)

class TooManyRequestsException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=429, detail=detail)

class RequestHeaderFieldsTooLargeException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=431, detail=detail)

class NoResponseException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=444, detail=detail)

class UnavailableForLegalReasonsException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=451, detail=detail)