from core.config import settings
from core.middleware.security import setup_security_middleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware


def setup_middleware(app: FastAPI) -> None:
    """Register all middlewares for application"""

    # Trusted hosts (защита от Host header attacks)
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=[
            # "xizmatdev.imv.uz",
            "localhost",
            "127.0.0.1",
        ],
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS.split(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Sessions
    app.add_middleware(
        SessionMiddleware,
        secret_key=settings.SECRET_KEY,
    )