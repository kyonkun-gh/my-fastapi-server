from pydantic import BaseModel

class RequestModel(BaseModel):
    url: str
    method: str
    data: str