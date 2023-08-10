import sqlite3
from datetime import datetime
from random import randint, choice

import faker

from create_db import engine

# NUMBER_STUDENTS = 50
# NUMBER_FACULTIES = 3
# NUMBER_PROFESSORS = 5
# NUMBER_SUBJECTS = 8
# NUMBER_GRADES = 20
# LEVEL_GRADES = 5

NUMBER_STUDENTS = 2
NUMBER_FACULTIES = 2
NUMBER_PROFESSORS = 2
NUMBER_SUBJECTS = 2
NUMBER_GRADES = 4
LEVEL_GRADES = 5


def generate_fake_data(
    number_students, number_faculties, number_professors, number_subjects, number_grades
) -> tuple():
    fake_students = []
    fake_faculties = []
    fake_professors = []
    fake_subjects = []

    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(
            (
                fake_data.last_name(),
                fake_data.first_name(),
                fake_data.unique.ascii_email(),
            )
        )

    for _ in range(number_faculties):
        fake_faculties.append(fake_data.job())

    for _ in range(number_professors):
        fake_professors.append(
            (
                fake_data.last_name(),
                fake_data.first_name(),
            )
        )

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    fake_grades = [randint(1, LEVEL_GRADES) for _ in range(number_grades)]

    return fake_students, fake_faculties, fake_professors, fake_subjects, fake_grades


def prepare_data(students, faculties, professors, subjects, grades) -> dict():
    for_students = []
    for student in students:
        for_students.append(
            # (student[0], student[1], student[2], randint(1, NUMBER_FACULTIES))
            {student[0], student[1], student[2], randint(1, NUMBER_FACULTIES)}
        )

    for_faculties = []
    for faculty in faculties:
        for_faculties.append((faculty,))

    for_professors = []
    for professor in professors:
        for_professors.append((professor[0], professor[1]))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_PROFESSORS)))

    for_grades = []
    for student in range(1, NUMBER_STUDENTS + 1):
        for _ in grades:
            assessment_date = datetime(2023, randint(1, 6), randint(1, 28)).date()
            for_grades.append(
                (student, randint(1, NUMBER_SUBJECTS), choice(grades), assessment_date)
            )

    return for_students, for_faculties, for_professors, for_subjects, for_grades


def insert_data_to_db(students, faculties, professors, subjects, grades) -> None:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()

        sql_to_students = """INSERT INTO students (last_name, first_name, e_mail, faculty_id) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_faculties = """INSERT INTO faculties(name) VALUES (?)"""
        cur.executemany(sql_to_faculties, faculties)

        sql_to_professors = (
            """INSERT INTO professors (last_name, first_name) VALUES (?, ?)"""
        )
        cur.executemany(sql_to_professors, professors)

        sql_to_subjects = """INSERT INTO subjects(title, professor_id) VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_marks = """INSERT INTO marks(student_id, subject_id, mark, date_of) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, grades)

        con.commit()


if __name__ == "__main__":
    students, faculties, professors, subjects, grades = prepare_data(
        *generate_fake_data(
            NUMBER_STUDENTS,
            NUMBER_FACULTIES,
            NUMBER_PROFESSORS,
            NUMBER_SUBJECTS,
            NUMBER_GRADES,
        ),
    )
    print(students, faculties, professors, subjects, grades)
    # insert_data_to_db(students, faculties, professors, subjects, grades)
