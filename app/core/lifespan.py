import logging
from contextlib import asynccontextmanager

from admin import setup_admin
from fastapi import FastAPI
from logging_config import setup_logging


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        setup_logging()
        setup_admin(app)

        logger.info("✅ App starting up...")
        yield

    except Exception as e:
        logger.exception(f"Startup error: {e}")
        raise

    finally:
        logger.info("🔴 Shutting down app...")