import logging

import anyio
from core.minio import minio_client
from core.redis import redis_client
from db.session import session_factory
from fastapi import APIRouter
from sqlalchemy import text
from starlette.responses import JSONResponse

logger = logging.getLogger(__name__)

health_router = APIRouter()


@health_router.get("/health")
async def health_check():
    # Redis check
    try:
        pong = await redis_client.ping()
        redis_ok = pong is True
        logger.info("Redis is reachable")
    except Exception as e:
        logger.error(f"Redis error: {e}")
        return JSONResponse(status_code=503, content={"status": "redis-unreachable"})

    # MinIO check
    try:
        await anyio.to_thread.run_sync(minio_client.client.list_buckets)
        logger.info("MinIO is reachable")
    except Exception as e:
        logger.error(f"MinIO error: {e}")
        return JSONResponse(status_code=503, content={"status": "minio-unreachable"})

    # PostgreSQL check
    try:
        async with session_factory() as session:
            await session.execute(text("SELECT 1"))
            logger.info("PostgreSQL is reachable")
    except Exception as e:
        logger.error(f"PostgreSQL error: {e}")
        return JSONResponse(status_code=503, content={"status": "postgres-unreachable"})

    return {"status": "ok"}