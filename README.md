# Запуск
1. Установить зависимости `pip install -R requirements.txt`
2. Прописать миграции `alembic revision --autogenerate -m "Initial"`
`alembic upgrade head`
3. Запустить приложение `unicorn main:app --reload`

# Инициализация базы данных
Выполнить `python db_init.py`
