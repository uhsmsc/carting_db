from sqlalchemy import Column, Integer, String, ForeignKey, \
    Boolean, CheckConstraint, text, DateTime
from sqlalchemy.dialects.postgresql import TIMESTAMP
from src.database import Base, metadata
from src.races.models import Track


class Client(Base):
    __tablename__ = "clients"
    metadata = metadata

    id = Column(Integer, primary_key=True, autoincrement=True, server_default="1")
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)


class Reservation(Base):
    __tablename__ = "reservations"
    metadata = metadata

    id = Column(Integer, primary_key=True, autoincrement=True, server_default="1")
    id_client = Column(
        Integer,
        ForeignKey(
            "clients.id",
            ondelete="Cascade",
            onupdate="Cascade"
        ), nullable=False)
    timestart = Column(DateTime, nullable=False)
    track_id = Column(
        Integer,
        ForeignKey(
            Track.id,
            ondelete="set null"
        ),
        nullable=True
    )
    count_drivers = Column(Integer, nullable=False, server_default="1")
    count_slots = Column(Integer, nullable=False, server_default="1")
    approved = Column(Boolean, nullable=True, server_default="false")
    price = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint(
            text('price > 0'),
            name='control_price'
        ),
        CheckConstraint(
            text('count_slots > 0'),
            name='control_count_slots'
        ),
        CheckConstraint(
            text('count_drivers > 0'),
            name='control_count_drivers'
        ),
    )
