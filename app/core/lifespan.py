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

        try:
            setup_admin(app)
            logger.info("🛠 Admin mounted successfully.")
        except Exception as admin_error:
            logger.error(f"❌ Admin startup error: {admin_error}")

        logger.info("✅ App starting up...")
        yield

    except Exception as e:
        logger.exception(f"Startup error: {e}")
        raise

    finally:
        logger.info("🔴 Shutting down app...")