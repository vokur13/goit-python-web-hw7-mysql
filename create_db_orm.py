from datetime import datetime
from random import randint, choice

import faker

from decouple import config

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import sessionmaker, declarative_base, relationship

db_user = config("DATABASE_USER", default="root")
db_pass = config("DATABASE_PASSWORD", default="password")
db_host = config("DATABASE_HOST", default="localhost")
db_port = config("DATABASE_PORT", default="3306")

NUMBER_STUDENTS = 50
NUMBER_FACULTIES = 3
NUMBER_PROFESSORS = 5
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 20
LEVEL_GRADES = 5

# NUMBER_STUDENTS = 5
# NUMBER_FACULTIES = 5
# NUMBER_PROFESSORS = 2
# NUMBER_SUBJECTS = 2
# NUMBER_GRADES = 4
# LEVEL_GRADES = 5

engine = create_engine(
    f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/university",
    echo=True,
)

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()

fake_data = faker.Faker()


class Faculty(Base):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True)
    name = Column(String(56))
    created_at = Column(DateTime, default=datetime.now())


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(56))
    first_name = Column(String(56))
    e_mail = Column(String(128), nullable=False, unique=True)
    faculty_id = Column(Integer, ForeignKey("faculties.id"))
    faculty = relationship(Faculty)
    created_at = Column(DateTime, default=datetime.now())


class Professor(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(56))
    first_name = Column(String(56))
    created_at = Column(DateTime, default=datetime.now())


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    title = Column(String(56))
    professor_id = Column(Integer, ForeignKey("professors.id"), nullable=False)
    professor = relationship(Professor)
    created_at = Column(DateTime, default=datetime.now())


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship(Student)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    subject = relationship(Subject)
    grade = Column(Integer)
    date_of = Column(DateTime, nullable=False)


name = fake_data.job()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    for _ in range(NUMBER_FACULTIES):
        faculty = Faculty(name=fake_data.job())
        session.add(faculty)

    for _ in range(NUMBER_STUDENTS):
        student = Student(
            last_name=fake_data.last_name(),
            first_name=fake_data.first_name(),
            e_mail=fake_data.unique.ascii_email(),
            faculty_id=randint(1, NUMBER_FACULTIES),
        )
        session.add(student)

    for _ in range(NUMBER_PROFESSORS):
        professor = Professor(
            last_name=fake_data.last_name(),
            first_name=fake_data.first_name(),
        )
        session.add(professor)

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
