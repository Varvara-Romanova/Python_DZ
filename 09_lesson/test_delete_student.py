# test_delete_student.py
from sqlalchemy import create_engine, text

# Подключение
db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string, echo=True)


def test_delete_student():
    # Уникальный user_id
    user_id = 999997

    # Добавляем
    db.execute(
        text("""
            INSERT INTO student (user_id, level, education_form, subject_id)
            VALUES (:user_id, 'elementary', 'part-time', 789)
        """),
        {"user_id": user_id}
    )

    exists_before = db.execute(
        text("SELECT COUNT(*) FROM student WHERE user_id = :user_id"),
        {"user_id": user_id}
    ).scalar()

    assert exists_before == 1

    # Удаляем
    db.execute(
        text("DELETE FROM student WHERE user_id = :user_id"),
        {"user_id": user_id}
    )

    # Проверяем, что удалился
    exists_after = db.execute(
        text("SELECT COUNT(*) FROM student WHERE user_id = :user_id"),
        {"user_id": user_id}
    ).scalar()

    assert exists_after == 0
