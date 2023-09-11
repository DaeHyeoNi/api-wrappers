import os
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class APIKeyMiddleWares(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        headers = dict(request.headers)
        if headers.get("x-api-key") == os.environ.get("PRIVATE_API_KEY"):
            return await call_next(request)
        else:
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})
