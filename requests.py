# Основные запросы

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.races.models import Track
from src.reservations.models import Client, Reservation

# Создаем подключение к базе данных
engine = create_engine("postgresql://postgres:postgres@localhost/carting")
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Вывести всех клиентов
    def print_all_clients():
        clients = session.query(Client).all()
        for client in clients:
            print(f"Client ID: {client.id}, Name: {client.name}, Phone: {client.phone}")

    # Вывести все бронирования
    def print_all_reservations():
        reservations = session.query(Reservation).all()
        for reservation in reservations:
            print(f"Reservation ID: {reservation.id}, Client ID: {reservation.id_client}, Track ID: {reservation.track_id}, Start Time: {reservation.timestart}")

    # Вывести все трассы
    def print_all_tracks():
        tracks = session.query(Track).all()
        for track in tracks:
            print(f"Track ID: {track.id}, Name: {track.name}, Model: {track.model}")

    # Добавить клиента
    def add_client(name, phone):
        new_client = Client(name=name, phone=phone)
        session.add(new_client)
        session.commit()

    # Вызов функций
    print("All Clients:")
    print_all_clients()

    print("\nAll Reservations:")
    print_all_reservations()

    print("\nAll Tracks:")
    print_all_tracks()

    print("\nAdding a new client...")
    new_client_name = input("ФИО клиента: ")
    new_client_phone = input("Телефон клиента: ")
    add_client("Новый клиент", "1234567890")
    print("New client added successfully.")

finally:
    # Закрываем сессию
    session.close()
