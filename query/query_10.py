# Список курсов, которые определенному студенту читает определенный преподаватель.

from sqlalchemy import select, func

from connect_db import session
from models import Student, Professor, Subject, Grade

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(
                Student.last_name,
                Student.first_name,
                Professor.last_name,
                Professor.first_name,
                Subject.title,
            )
            .select_from(Student)
            .join(Grade, Student.id == Grade.student_id)
            .join(Subject, Subject.id == Grade.subject_id)
            .join(Professor, Professor.id == Subject.professor_id)
            .filter(Student.id == 2)
            .filter(Professor.id == 2)
            .group_by(Student.last_name, Student.first_name, Subject.title)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)

# SELECT s1.last_name, s1.first_name, p.last_name, p.first_name, title
# FROM students s1
#          INNER JOIN main.marks m on s1.id = m.student_id
#          INNER JOIN main.subjects s on s.id = m.subject_id
#          INNER JOIN main.professors p on p.id = s.professor_id
# WHERE s1.id = '?'
#   AND p.id = '?';
