from datetime import datetime

import faker

from decouple import config

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    select,
)


db_user = config("DATABASE_USER", default="root")
db_pass = config("DATABASE_PASSWORD", default="password")
db_host = config("DATABASE_HOST", default="localhost")
db_port = config("DATABASE_PORT", default="3306")

engine = create_engine(
    f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/university",
    echo=True,
)


fake_data = faker.Faker()

metadata = MetaData()


faculties = Table(
    "faculties",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(56)),
    Column("created_at", DateTime, default=datetime.now()),
)

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("last_name", String(56), nullable=False),
    Column("first_name", String(56), nullable=False),
    Column("e_mail", String(128), nullable=False, unique=True),
    Column("faculty_id", Integer, ForeignKey("faculties.id"), nullable=False),
    Column("created_at", DateTime, default=datetime.now()),
)


professors = Table(
    "professors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("last_name", String(56), nullable=False),
    Column("first_name", String(56), nullable=False),
    Column("created_at", DateTime, default=datetime.now()),
)


subjects = Table(
    "subjects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(56), nullable=False),
    Column("professor_id", Integer, ForeignKey("professors.id"), nullable=False),
    Column("created_at", DateTime, default=datetime.now()),
)


grades = Table(
    "grades",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("subject_id", Integer, ForeignKey("subjects.id")),
    Column("date_of", DateTime, nullable=False),
)


if __name__ == "__main__":
    metadata.create_all(engine)

    with engine.connect() as conn:
        ins = faculties.insert().values(name=fake_data.job())
        print(str(ins))
        result = conn.execute(ins)

        s = select(faculties)
        result = conn.execute(s)
        for row in result:
            print(row)  # (1, u'jack', u'Jack Jones')

        conn.commit()
