from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.responses import JSONResponse
from app.handler.server_exceptions import *

router = APIRouter(
    prefix="/server",
    tags=["SERVER EXCEPTIONS"],
    responses={404: {"message": "Not found"}}
)

@router.get("/500")
async def internal_server_error():
    raise InternalServerErrorException(detail='Hello World')

@router.get("/501")
async def not_implemented():
    raise NotImplementedException(detail='Hello World')

@router.get("/502")
async def bad_gateway():
    raise BadGatewayException(detail='Hello World')

@router.get("/503")
async def service_unavailable():
    raise ServiceUnavailableException(detail='Hello World')

@router.get("/504")
async def gateway_timeout():
    raise GatewayTimeoutException(detail='Hello World')

@router.get("/505")
async def http_version_not_supported():
    raise HTTPVersionNotSupportedException(detail='Hello World')

@router.get("/506")
async def variant_also_negotiates():
    raise VariantAlsoNegotiatesException(detail='Hello World')

@router.get("/507")
async def insufficient_storage():
    raise InsufficientStorageException(detail='Hello World')

@router.get("/508")
async def loop_detected():
    raise LoopDetectedException(detail='Hello World')

@router.get("/510")
async def not_extended():
    raise NotExtendedException(detail='Hello World')

@router.get("/511")
async def network_authentication_required():
    raise NetworkAuthenticationRequiredException(detail='Hello World')

