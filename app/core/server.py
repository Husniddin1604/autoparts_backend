import uvicorn
from core.config import settings


def get_config():
    if settings.APP_MODE == "PRODUCTION":
        # if needed to use workers, it's recommended to use uvicorn CLI,
        # because uvicorn in Python script will run in Python script's process
        # and workers will be added under this process
        # It will complicate managing worker processes
        # Best practice is to use Gunicorn with uvicorn workers through CLI

        return {
            "log_level": "warning",
            "access_log": False,
            "forwarded_allow_ips": "*",
        }
    elif settings.APP_MODE == "DEVELOPMENT":
        return {
            "log_level": "debug",
            "forwarded_allow_ips": "*",
        }
    else:
        return {
            "reload": True,
            "log_level": "debug",
            "forwarded_allow_ips": "*",
        }

def run():
    config = get_config()
    uvicorn.run(
        app="app.main:app",
        host="0.0.0.0",
        port=9090,
        loop="uvloop",
        **config
    )