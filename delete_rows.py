from connect_db import session
from models import Faculty, Student, Professor, Subject, Grade


if __name__ == "__main__":
    grades = session.query(Grade).all()
    for grade in grades:
        session.delete(grade)

    subjects = session.query(Subject).all()
    for subject in subjects:
        session.delete(subject)

    students = session.query(Student).all()
    for student in students:
        session.delete(student)

    faculties = session.query(Faculty).all()
    for faculty in faculties:
        session.delete(faculty)

    professors = session.query(Professor).all()
    for professor in professors:
        session.delete(professor)

    session.commit()
