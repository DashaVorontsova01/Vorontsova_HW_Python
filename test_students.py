import pytest
from sqlalchemy import create_engine, text, inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.exc import SQLAlchemyError
import logging

# Настройка подключения к базе данных
# Экранируем символ @ в пароле с помощью URL-кодирования
db_connection_string = "postgresql://postgres:Masterit%402024@localhost:5432/postgres"
db = create_engine(db_connection_string)

# Настройка логирования для отладки
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_module(module):
    # Создание тестовой таблицы перед выполнением тестов.
    try:
        with db.connect() as connection:
            # Создаем таблицу students, если она не существует
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INTEGER,
                    course VARCHAR(50)
                )
            """))
            connection.commit()
            logger.info("Тестовая таблица students создана или уже существует")
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при создании таблицы: {e}")
        raise

def teardown_module(module):
    try:
        with db.connect() as connection:
            # Удаляем все записи из таблицы students
            connection.execute(text("DELETE FROM students"))
            connection.commit()
            logger.info("Тестовые данные очищены")
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при очистке данных: {e}")
        raise

def cleanup_student(student_id):
    # Вспомогательная функция для удаления тестовых данных.
    try:
        with db.connect() as connection:
            delete_query = text("DELETE FROM students WHERE id = :student_id")
            connection.execute(delete_query, {"student_id": student_id})
            connection.commit()
            logger.info(f"Студент с ID {student_id} удален")
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при удалении студента: {e}")
        raise

def test_db_connection():
    # Тест подключения к базе данных и проверка существования таблицы
    inspector = inspect(db)
    tables = inspector.get_table_names()

    # Проверяем, что таблица students существует
    assert 'students' in tables, "Таблица students не найдена в базе данных"

    logger.info("Тест подключения к БД выполнен успешно")


def test_add_student():
    # Тест добавления нового студента в базу данных.
    student_name = "Иван Иванов"
    student_age = 20
    student_course = "Информатика"

    try:
        with db.connect() as connection:
            # Добавляем нового студента
            insert_query = text("""
                INSERT INTO students (name, age, course) 
                VALUES (:name, :age, :course) 
                RETURNING id
            """)
            result = connection.execute(
                insert_query,
                {
                    "name": student_name,
                    "age": student_age,
                    "course": student_course
                }
            )
            connection.commit()

            # Получаем ID добавленного студента
            student_id = result.fetchone()[0]
            logger.info(f"Студент добавлен с ID: {student_id}")

            # Проверяем, что студент действительно добавлен
            select_query = text("SELECT * FROM students WHERE id = :student_id")
            student = connection.execute(
                select_query,
                {"student_id": student_id}
            ).fetchone()

            # Проверяем корректность данных
            assert student is not None, "Студент не найден после добавления"
            assert student[1] == student_name, "Имя студента не совпадает"
            assert student[2] == student_age, "Возраст студента не совпадает"
            assert student[3] == student_course, "Курс студента не совпадает"

            logger.info(f"Тест добавления студента выполнен: ID {student_id}")

            # Удаляем созданного студента (очистка)
            cleanup_student(student_id)

    except SQLAlchemyError as e:
        logger.error(f"Ошибка в тесте добавления студента: {e}")
        raise


def test_update_student():
    # Тест обновления данных студента.
    # Сначала создаем тестового студента
    try:
        with db.connect() as connection:
            # Добавляем студента для теста обновления
            insert_query = text("""
                INSERT INTO students (name, age, course) 
                VALUES (:name, :age, :course) 
                RETURNING id
            """)
            result = connection.execute(
                insert_query,
                {
                    "name": "Мария Петрова",
                    "age": 19,
                    "course": "Математика"
                }
            )
            connection.commit()
            student_id = result.fetchone()[0]

            logger.info(f"Создан студент для теста обновления: ID {student_id}")

            # Обновляем данные студента
            new_name = "Мария Сидорова"
            new_age = 20
            new_course = "Физика"

            update_query = text("""
                UPDATE students 
                SET name = :name, age = :age, course = :course 
                WHERE id = :student_id
            """)
            connection.execute(
                update_query,
                {
                    "name": new_name,
                    "age": new_age,
                    "course": new_course,
                    "student_id": student_id
                }
            )
            connection.commit()

            # Проверяем обновленные данные
            select_query = text("SELECT * FROM students WHERE id = :student_id")
            updated_student = connection.execute(
                select_query,
                {"student_id": student_id}
            ).fetchone()

            # Проверяем корректность обновления
            assert updated_student is not None, "Студент не найден после обновления"
            assert updated_student[1] == new_name, "Имя не обновлено корректно"
            assert updated_student[2] == new_age, "Возраст не обновлен корректно"
            assert updated_student[3] == new_course, "Курс не обновлен корректно"

            logger.info(f"Тест обновления студента выполнен: ID {student_id}")

            # Удаляем созданного студента (очистка)
            cleanup_student(student_id)

    except SQLAlchemyError as e:
        logger.error(f"Ошибка в тесте обновления студента: {e}")
        raise


def test_delete_student():
    # Тест удаления студента из базы данных.
    try:
        with db.connect() as connection:
            # Сначала создаем студента для теста удаления
            insert_query = text("""
                INSERT INTO students (name, age, course) 
                VALUES (:name, :age, :course) 
                RETURNING id
            """)
            result = connection.execute(
                insert_query,
                {
                    "name": "Алексей Смирнов",
                    "age": 21,
                    "course": "Химия"
                }
            )
            connection.commit()
            student_id = result.fetchone()[0]

            logger.info(f"Создан студент для теста удаления: ID {student_id}")

            # Удаляем студента
            delete_query = text("DELETE FROM students WHERE id = :student_id")
            connection.execute(delete_query, {"student_id": student_id})
            connection.commit()

            # Проверяем, что студент удален
            select_query = text("SELECT * FROM students WHERE id = :student_id")
            deleted_student = connection.execute(
                select_query,
                {"student_id": student_id}
            ).fetchone()

            # Проверяем, что студент больше не существует
            assert deleted_student is None, "Студент не был удален"

            logger.info(f"Тест удаления студента выполнен: ID {student_id}")

    except SQLAlchemyError as e:
        logger.error(f"Ошибка в тесте удаления студента: {e}")
        raise

if __name__ == "__main__":
    # Для запуска тестов без pytest (опционально)
    pytest.main([__file__, "-v"])