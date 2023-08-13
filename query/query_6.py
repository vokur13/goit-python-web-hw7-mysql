# Найти список студентов в определенной группе.

from sqlalchemy import select, func

from connect_db import session
from models import Student, Faculty

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(Faculty.name, Student.last_name, Student.first_name)
            .select_from(Faculty)
            .join(Student)
            .filter(Faculty.id == 1)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)

# SELECT f.name, s.last_name, s.first_name
# FROM faculties AS f
#          LEFT JOIN main.students s on f.id = s.faculty_id
# WHERE f.id = ?;
