from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.races.models import Track, Cart, Races
from src.reservations.models import Client, Reservation
from faker import Faker
import random
from datetime import datetime, timedelta

# Подключение к базе данных
engine = create_engine("postgresql://postgres:postgres@localhost:5432/carting")
Session = sessionmaker(bind=engine)
session = Session()

# Создание экземпляра Faker
fake = Faker()

# Создание фейковых данных для моделей

# Фейковые данные для модели Track
def generate_fake_track():
    fake_track = {
        "model": fake.word(),
        "length": random.randint(350, 1000),
        "name": fake.word(),
        "max_carts": random.randint(4, 10)
    }
    return fake_track

# Фейковые данные для модели Cart
def generate_fake_cart(track_id):
    fake_cart = {
        "model": fake.word(),
        "number": random.randint(0, 100),
        "isready": True,
        "track_id": track_id
    }
    return fake_cart

# Фейковые данные для модели Races
def generate_fake_race(track_id):
    fake_race = {
        "count_drivers": random.randint(1, 10),
        "timestart": datetime.now() + timedelta(days=random.randint(1, 30)),
        "full_load": False,
        "track_id": track_id
    }
    return fake_race

# Фейковые данные для модели Client
def generate_fake_client():
    fake_client = {
        "name": fake.name(),
        "phone": fake.phone_number()
    }
    return fake_client

# Фейковые данные для модели Reservation
def generate_fake_reservation(client_id, track_id):
    fake_reservation = {
        "id_client": client_id,
        "timestart": datetime.now() + timedelta(days=random.randint(1, 30)),
        "track_id": track_id,
        "count_drivers": random.randint(1, 4),
        "count_slots": random.randint(1, 4),
        "approved": False,
        "price": random.randint(100, 1000)
    }
    return fake_reservation

# Заполнение базы данных фейковыми данными
tracks = []
carts = []

# Заполнение моделей Track и Cart
for _ in range(10):
    fake_track = generate_fake_track()
    new_track = Track(**fake_track)
    session.add(new_track)
    session.commit()
    tracks.append(new_track)

    for _ in range(5):
        fake_cart = generate_fake_cart(new_track.id)
        new_cart = Cart(**fake_cart)
        session.add(new_cart)
        session.commit()
        carts.append(new_cart)

# Заполнение модели Races
for _ in range(5):
    track = random.choice(tracks)
    fake_race = generate_fake_race(track.id)
    new_race = Races(**fake_race)
    session.add(new_race)
    session.commit()

# Заполнение моделей Client и Reservation
clients = []
reservations = []

for _ in range(10):
    fake_client = generate_fake_client()
    new_client = Client(**fake_client)
    session.add(new_client)
    session.commit()
    clients.append(new_client)

    for _ in range(3):
        track = random.choice(tracks)
        fake_reservation = generate_fake_reservation(new_client.id, track.id)
        new_reservation = Reservation(**fake_reservation)
        session.add(new_reservation)
        session.commit()
        reservations.append(new_reservation)

# Закрытие сессии
session.close()

print("База данных успешно заполнена фейковыми данными.")
