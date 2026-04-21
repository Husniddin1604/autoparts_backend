from core.config import settings
from fastapi import FastAPI, Request


def setup_security_middleware(app: FastAPI):
    @app.middleware("http")
    async def https_middleware(request: Request, call_next):
        x_forwarded_proto = request.headers.get("x-forwarded-proto")
        if settings.APP_MODE == "PRODUCTION":
            is_production = "xizmat.uzasbo.uz" in str(request.url)
        else:
            is_production = "xizmatdev.imv.uz" in str(request.url)

        if x_forwarded_proto == "https" or is_production:
            scope = dict(request.scope)
            scope["scheme"] = "https"

            if "x-forwarded-host" in request.headers:
                scope["headers"] = [
                    (b"host", request.headers["x-forwarded-host"].encode()),
                    *[(k, v) for k, v in request.scope["headers"] if k != b"host"],
                ]
            request = Request(scope, request.receive)

        response = await call_next(request)

        response.headers[
            "Strict-Transport-Security"
        ] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"] = (
            "upgrade-insecure-requests; "
            "default-src 'self' https: http:; "  # Added http:
            "script-src 'self' https: 'unsafe-inline' 'unsafe-eval'; "
            "style-src 'self' https: 'unsafe-inline'; "
            "style-src-elem 'self' https: 'unsafe-inline'; "
            "img-src 'self' https: data: blob:; "
            "font-src 'self' https: data:; "
            "connect-src 'self' https: http:;"  # Added http:
            "frame-ancestors 'self';"
        )

        return response