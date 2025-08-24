from datetime import date
from typing import List

from pydantic import BaseModel

class BookingDates(BaseModel):
    checkin: date
    checkout: date

class BookingResponse(BaseModel):
    bookingid: int
    roomid: int
    firstname: str
    lastname: str
    depositpaid: bool
    bookingdates: BookingDates


class BookingListResponse(BaseModel):
    bookings: List[BookingResponse]
