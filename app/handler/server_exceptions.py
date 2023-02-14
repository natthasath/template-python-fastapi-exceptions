from typing import Any
from fastapi.exception_handlers import HTTPException

class InternalServerErrorException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=500, detail=detail)

class NotImplementedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=501, detail=detail)

class BadGatewayException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=502, detail=detail)

class ServiceUnavailableException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=503, detail=detail)

class GatewayTimeoutException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=504, detail=detail)

class HTTPVersionNotSupportedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=505, detail=detail)

class VariantAlsoNegotiatesException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=506, detail=detail)

class InsufficientStorageException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=507, detail=detail)

class LoopDetectedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=508, detail=detail)

class NotExtendedException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=510, detail=detail)

class NetworkAuthenticationRequiredException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=511, detail=detail)