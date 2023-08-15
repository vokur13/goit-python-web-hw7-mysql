from connect_db import session
from models import Faculty, Student, Professor, Subject, Grade

from random import randint, choice
from datetime import datetime


import faker

fake_data = faker.Faker()

NUMBER_STUDENTS = 50
NUMBER_FACULTIES = 3
NUMBER_PROFESSORS = 5
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 20
LEVEL_GRADES = 5


if __name__ == "__main__":
    for _ in range(NUMBER_FACULTIES):
        faculty = Faculty(name=fake_data.job())
        session.add(faculty)

    for _ in range(NUMBER_PROFESSORS):
        professor = Professor(
            last_name=fake_data.last_name(),
            first_name=fake_data.first_name(),
        )
        session.add(professor)

    for _ in range(NUMBER_STUDENTS):
        student = Student(
            last_name=fake_data.last_name(),
            first_name=fake_data.first_name(),
            e_mail=fake_data.unique.ascii_email(),
            faculty_id=randint(1, NUMBER_FACULTIES),
        )
        session.add(student)

    for _ in range(NUMBER_SUBJECTS):
        subject = Subject(
            title=fake_data.job(), professor_id=randint(1, NUMBER_PROFESSORS)
        )
        session.add(subject)

    for student in range(1, NUMBER_STUDENTS + 1):
        for _ in [randint(1, LEVEL_GRADES) for _ in range(NUMBER_GRADES)]:
            assessment_date = datetime(2023, randint(1, 6), randint(1, 28)).date()
            grade = Grade(
                student_id=student,
                subject_id=randint(1, NUMBER_SUBJECTS),
                grade=choice([randint(1, LEVEL_GRADES) for _ in range(NUMBER_GRADES)]),
                date_of=assessment_date,
            )
            session.add(grade)

    session.commit()
