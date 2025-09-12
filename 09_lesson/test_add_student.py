from sqlalchemy import create_engine, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string, echo=True)


def test_add_student():
    user_id = 999999
    level = "intermediate"
    education_form = "part-time"
    subject_id = 456

    with db.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO student (user_id, level, education_form, subject_id)
                VALUES (:user_id, :level, :education_form, :subject_id)
            """),
            {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id
            }
        )

    # Проверка
    with db.connect() as conn:
        result = conn.execute(
            text("SELECT level, education_form, subject_id FROM student WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
        row = result.fetchone()

    assert row is not None
    assert row.level == level
    assert row.education_form == education_form
    assert row.subject_id == subject_id

    # Удаление
    with db.begin() as conn:
        conn.execute(
            text("DELETE FROM student WHERE user_id = :user_id"),
            {"user_id": user_id}
        )
