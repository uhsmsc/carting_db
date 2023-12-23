from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, \
    Boolean, CheckConstraint, text

from src.database import Base, metadata


class Track(Base):
    __tablename__ = 'track'
    metadata = metadata

    id = Column(Integer, primary_key=True, autoincrement=True, server_default="1")
    model = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    max_carts = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint(
            text('max_carts >= 4'),
            name='control_max_carts'
        ),
        CheckConstraint(
            text('length >= 350'),
            name='control_length'
        ),
    )


class Cart(Base):
    __tablename__ = 'cart'
    metadata = metadata

    id = Column(Integer, primary_key=True, autoincrement=True, server_default="1")
    model = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    isready = Column(Boolean, nullable=False, server_default="True")
    track_id = Column(
        Integer,
        ForeignKey(
            "track.id",
            ondelete="set null"
        ),
        nullable=True
    )

    __table_args__ = (
        CheckConstraint(
            text('number >= 0'),
            name='control_number'
        ),
    )

class Races(Base):
    __tablename__ = 'races'

    metadata = metadata

    id = Column(Integer, primary_key=True, autoincrement=True, server_default="1")
    count_drivers = Column(Integer)
    timestart = Column(TIMESTAMP)
    full_load = Column(Boolean, nullable=False, server_default="False")
    track_id = Column(
        Integer,
        ForeignKey(
            "track.id",
            ondelete="set null"
        ),
        nullable=True
    )

    __table_args__ = (
        CheckConstraint(
            text('count_drivers >= 1'),
            name='control_drivers'
        ),
    )
