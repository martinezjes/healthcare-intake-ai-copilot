from pydantic import BaseModel
from typing import Any, Optional, Dict


class APIResponse(BaseModel):
    status: str
    message: Optional[str] = None
    data: Any = None
    meta: Optional[Dict[str, Any]] = None