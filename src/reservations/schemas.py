from datetime import datetime, timezone
from typing import Optional, List, Union

from pydantic import BaseModel, validator


class InsertClientShema(BaseModel):
    name: str
    phone: str

class ClientShema(InsertClientShema):
    id: int


class InsertReservationSchema(BaseModel):
    id_client: int
    timestart: datetime = datetime.now()
    track_id: Optional[int]
    count_drivers: int
    count_slots: int
    approved: bool = False
    price: int



class ReservationsSchema(InsertReservationSchema):
    id: int


class StandartResponseSchema(BaseModel):
    status: str
    data: Optional[List[ClientShema | ReservationsSchema]]
    message: Optional[str]

