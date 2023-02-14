from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.responses import JSONResponse
from app.handler.client_exceptions import *

router = APIRouter(
    prefix="/client",
    tags=["CLIENT EXCEPTIONS"],
    responses={404: {"message": "Not found"}}
)

@router.get("/400")
async def bad_request():
    raise BadRequestException(detail='Hello World')

@router.get("/401")
async def unauthorized():
    raise UnauthorizedException(detail='Hello World')

@router.get("/402")
async def payment_required():
    raise PaymentRequiredException(detail='Hello World')

@router.get("/403")
async def forbidden():
    raise ForbiddenException(detail='Hello World')

@router.get("/404")
async def not_found():
    raise NotFoundException(detail='Hello World')

@router.get("/405")
async def method_not_allowed():
    raise MethodNotAllowedException(detail='Hello World')

@router.get("/406")
async def not_acceptable():
    raise NotAcceptableException(detail='Hello World')

@router.get("/407")
async def proxy_authentication_required():
    raise ProxyAuthenticationRequiredException(detail='Hello World')

@router.get("/408")
async def request_timeout():
    raise RequestTimeoutException(detail='Hello World')

@router.get("/409")
async def conflict():
    raise ConflictException(detail='Hello World')

@router.get("/410")
async def gone():
    raise GoneException(detail='Hello World')

@router.get("/411")
async def length_required():
    raise LengthRequiredException(detail='Hello World')

@router.get("/412")
async def precondition_failed():
    raise PreconditionFailedException(detail='Hello World')

@router.get("/413")
async def payload_too_large():
    raise PayloadTooLargeException(detail='Hello World')

@router.get("/414")
async def uri_too_long():
    raise URITooLongException(detail='Hello World')

@router.get("/415")
async def unsupported_media_type():
    raise UnsupportedMediaTypeException(detail='Hello World')

@router.get("/416")
async def range_not_satisfiable():
    raise RangeNotSatisfiableException(detail='Hello World')

@router.get("/417")
async def expectation_failed():
    raise ExpectationFailedException(detail='Hello World')

@router.get("/418")
async def im_a_teapot():
    raise ImATeapotException(detail='Hello World')

@router.get("/421")
async def misdirected_request():
    raise MisdirectedRequestException(detail='Hello World')

@router.get("/422")
async def unprocessable_entity():
    raise UnprocessableEntityException(detail='Hello World')

@router.get("/423")
async def locked():
    raise LockedException(detail='Hello World')

@router.get("/424")
async def failed_dependency():
    raise FailedDependencyException(detail='Hello World')

@router.get("/425")
async def too_early():
    raise TooEarlyException(detail='Hello World')

@router.get("/426")
async def upgrade_required():
    raise UpgradeRequiredException(detail='Hello World')

@router.get("/428")
async def precondition_required():
    raise PreconditionRequiredException(detail='Hello World')

@router.get("/429")
async def tooMany_requests():
    raise TooManyRequestsException(detail='Hello World')

@router.get("/431")
async def request_header_fields_too_large():
    raise RequestHeaderFieldsTooLargeException(detail='Hello World')

@router.get("/444")
async def no_response():
    raise NoResponseException(detail='Hello World')

@router.get("/451")
async def unavailable_for_legal_reasons():
    raise UnavailableForLegalReasonsException(detail='Hello World')