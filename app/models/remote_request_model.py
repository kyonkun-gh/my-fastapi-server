from pydantic import BaseModel
from typing import Dict, Any

class RemoteRequestModel(BaseModel):
    remote_url: str
    remote_method: str
    remote_data: Dict[str, Any]