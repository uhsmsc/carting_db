from fastapi import APIRouter, Depends
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.reservations.models import Client, Reservation
from src.reservations.schemas import StandartResponseSchema, \
     InsertClientShema, InsertReservationSchema
from src.reservations.utils import get_answer_format

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)


@router.get("/get_all_clients", response_model=StandartResponseSchema)
async def get_all_clients(
        session: AsyncSession = Depends(get_async_session)
):
    try:
        stmt = (
            select(Client)
        )
        res = await session.execute(stmt)
        clients = res.scalars()
        answer = get_answer_format(clients)
        return {"status": "success", "data": answer, "message": None}
    except Exception as e:
        return {"status": "error", "data": None, "message": str(e)}


@router.post("/insert_client", response_model=StandartResponseSchema)
async def insert_client(
        client: InsertClientShema,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        new_client = Client(name=client.name, phone=client.phone)
        session.add(new_client)
        await session.commit()
        return {"status": "success", "data": None, "message": "New client added"}
    except Exception as e:
        await session.rollback()
        return {"status": "error", "data": None, "message": str(e)}


@router.get("/get_all_reservations", response_model=StandartResponseSchema)
async def get_all_reservations(
        session: AsyncSession = Depends(get_async_session)
):
    try:
        stmt = (select(Reservation))
        res = await session.execute(stmt)
        reservations = res.scalars()
        answer = get_answer_format(reservations)
        return {"status": "success", "data": answer, "message": None}
    except Exception as e:
        return {"status": "error", "data": None, "message": str(e)}


@router.post("/insert_reservation", response_model=StandartResponseSchema)
async def insert_reservation(
        reservation: InsertReservationSchema,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        new_reservation = Reservation(
            id_client=reservation.id_client,
            timestart=reservation.timestart,
            count_drivers=reservation.count_drivers,
            track_id=reservation.track_id,
            count_slots=reservation.count_slots,
            approved=reservation.approved,
            price=reservation.price
        )

        session.add(new_reservation)  # Добавляем бронирование в сессию
        await session.commit()
        return {"status": "success", "data": None, "message": "New reservation"}
    except Exception as e:
        await session.rollback()
        return {"status": "error", "data": None, "message": str(e)}


@router.put("/approve_reservation")
async def approve_reservation(
        id_reservation: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        result = await session.execute(select(Reservation).where(
            Reservation.id == id_reservation))
        reservation = result.scalar()
        if reservation is None:
            return {"status": "fail", "message": "Reservation does not exist"}
        await session.execute(update(Reservation).where(
            Reservation.id == id_reservation).values(approved=True))
        await session.commit()

        return {
            "status": "success", "message": "Reservation approved"
        }
    except Exception as e:
        await session.rollback()
        return {"status": "error", "message": str(e)}