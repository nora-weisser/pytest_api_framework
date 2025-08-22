from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class RoomResponse(BaseModel):
    roomid: int
    roomName: str
    type: str
    description: Optional[str]
    accessible: bool
    image: str
    features: List[str]
    roomPrice: int

class RoomListResponse(BaseModel):
    rooms: List[RoomResponse]
