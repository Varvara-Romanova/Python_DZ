# test_update_student.py
from sqlalchemy import create_engine, text

# Подключение
db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string, echo=True)


def test_update_student():
    # Уникальный user_id
    user_id = 999998

    db.execute(
        text("""
            INSERT INTO student (user_id, level, education_form, subject_id)
            VALUES (:user_id, 'beginner', 'full-time', 123)
        """),
        {"user_id": user_id}
    )

    # Обновляем
    new_level = "advanced"
    new_education_form = "distance"

    db.execute(
        text("""
            UPDATE student
            SET level = :level, education_form = :education_form
            WHERE user_id = :user_id
        """),
        {"level": new_level, "education_form": new_education_form, "user_id": user_id}
    )

    # Проверяем
    result = db.execute(
        text("SELECT level, education_form FROM student WHERE user_id = :user_id"),
        {"user_id": user_id}
    )
    row = result.fetchone()

    assert row is not None
    assert row.level == new_level
    assert row.education_form == new_education_form

    # Удаляем
    db.execute(
        text("DELETE FROM student WHERE user_id = :user_id"),
        {"user_id": user_id}
    )
