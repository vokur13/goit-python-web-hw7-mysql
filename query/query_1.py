# -- Найти 5 студентов с наибольшим средним баллом по всем предметам.

from sqlalchemy import select, func, desc


from connect_db import session
from models import Student, Grade

if __name__ == "__main__":
    stmt = session.execute(
        select(
            Student.last_name,
            Student.first_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
    ).mappings()

    for item in stmt:
        print(item)
