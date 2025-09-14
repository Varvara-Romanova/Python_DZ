# test_db_connection.py
from sqlalchemy import create_engine, inspect

# Подключение
db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string, echo=True)


def test_db_connection():
    """Проверяем, что подключение работает и таблицы есть"""
    inspector = inspect(db)
    table_names = inspector.get_table_names()
    assert 'student' in table_names
    assert 'app_users' in table_names
