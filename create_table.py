"""
Зробити такі вибірки з отриманої бази даних:

Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

Знайти студента із найвищим середнім балом з певного предмета.
Знайти середній бал у групах з певного предмета.
Знайти середній бал на потоці (по всій таблиці оцінок).
Знайти які курси читає певний викладач.
Знайти список студентів у певній групі.
Знайти оцінки студентів у окремій групі з певного предмета.
Знайти середній бал, який ставить певний викладач зі своїх предметів.
Знайти список курсів, які відвідує студент.
Список курсів, які певному студенту читає певний викладач.
"""

import sqlite3
from random import randint, choice

from faker import Faker

fake = Faker("uk-UA")

conn = sqlite3.connect("../university.db")

cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS students""")
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    group_id INTEGER,
                    FOREIGN KEY (group_id) REFERENCES groups (id)
                )
    """
)

cursor.execute("""DROP TABLE IF EXISTS groups""")
# Створення таблиці груп
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name NOT NULL
                )"""
)

cursor.execute("""DROP TABLE IF EXISTS teachers""")
# Створення таблиці викладачів
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )"""
)

cursor.execute("""DROP TABLE IF EXISTS subjects""")
# Створення таблиці предметів
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject TEXT NOT NULL,
                    teacher_id INTEGER,
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                )"""
)

cursor.execute("""DROP TABLE IF EXISTS grades""")
# Створення таблиці оцінок
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date DATETIME,
                    FOREIGN KEY (student_id) REFERENCES students(id) ON UPDATE CASCADE, 
                    FOREIGN KEY (subject_id) REFERENCES subjects(id) ON UPDATE CASCADE
                )"""
)

# Збереження змін у базі даних
conn.commit()

# Закриття з'єднання з базою даних
conn.close()

with sqlite3.connect("../university.db") as con:
    cur = con.cursor()

    sql_to_groups = """INSERT INTO groups (name) VALUES (?)"""
    for _ in range(1, 4):
        cur.execute(sql_to_groups, (fake.word(),))

    sql_to_teachers = """INSERT INTO teachers (name) VALUES (?)"""
    for _ in range(1, 6):
        cur.execute(sql_to_teachers, (fake.name(),))

    sql_to_subjects = """INSERT INTO subjects (subject, teacher_id) VALUES (?,?)"""
    for _ in range(1, 9):
        cur.execute(sql_to_subjects, (fake.word(), randint(1, 5),))

    for group_id in range(1, 4):
        for _ in range(10):
            cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?) RETURNING id",
                        (fake.name(), group_id))
            student_id = cur.fetchone()[0]
            for subject_id in range(1, 9):
                for _ in range(3):
                    cur.execute(
                        "INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                        (student_id, subject_id, randint(0, 100), fake.date_this_decade(),))
