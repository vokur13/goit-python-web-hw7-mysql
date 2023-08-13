# Найти список курсов, которые посещает определенный студент.

from sqlalchemy import select, func

from connect_db import session
from models import Student, Subject, Grade

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(
                Student.last_name,
                Student.first_name,
                Subject.title,
            )
            .select_from(Student)
            .join(Grade, Student.id == Grade.student_id)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(Student.id == 2)
            .group_by(Student.last_name, Student.first_name, Subject.title)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)

# SELECT s.last_name, s.first_name, title
# FROM students s
#          INNER JOIN main.marks m on s.id = m.student_id
#          INNER JOIN main.subjects s2 on s2.id = m.subject_id
# WHERE s.id = '?'
# GROUP BY s.last_name, s.first_name, title;
