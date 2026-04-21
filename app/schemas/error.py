from typing import Optional

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status_code: int
    error: str
    detail: Optional[str] = None
