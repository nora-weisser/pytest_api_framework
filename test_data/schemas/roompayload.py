from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class RoomPayload(BaseModel):
    roomName: str
    type: str
    description: Optional[str]
    accessible: bool
    image: HttpUrl
    features: List[str]
    roomPrice: int
