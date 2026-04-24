from pathlib import Path

import uvicorn
from core.config import settings
from app.logging_config import CUSTOM_LOGGING_CONFIG


def get_config():
    if settings.APP_MODE in ("PRODUCTION", "DEVELOPMENT"):
        # if needed to use workers, it's recommended to use uvicorn CLI,
        # because uvicorn in Python script will run in Python script's process
        # and workers will be added under this process
        # It will complicate managing worker processes
        # Best practice is to use Gunicorn with uvicorn workers through CLI

        return {
            "forwarded_allow_ips": "*",
        }

    else:
        reload_dir = Path(__file__).resolve().parent.parent
        return {
            "reload": True,
            "reload_dirs": [str(reload_dir)],
            "forwarded_allow_ips": "*",
        }

def apply_env_logging():
    if settings.APP_MODE == "PRODUCTION":
        level = "WARNING"
        access_level = "WARNING"   # отключаем access лог
    else:
        level = "DEBUG"
        access_level = "INFO"      # включаем access лог

    CUSTOM_LOGGING_CONFIG["loggers"][""]["level"] = level
    CUSTOM_LOGGING_CONFIG["loggers"]["uvicorn"]["level"] = level
    CUSTOM_LOGGING_CONFIG["loggers"]["uvicorn.error"]["level"] = level
    CUSTOM_LOGGING_CONFIG["loggers"]["uvicorn.access"]["level"] = access_level


def run():
    apply_env_logging()
    config = get_config()
    uvicorn.run(
        app="app.main:app",
        host="0.0.0.0",
        port=9090,
        loop="uvloop",
        log_config=CUSTOM_LOGGING_CONFIG,
        **config
    )