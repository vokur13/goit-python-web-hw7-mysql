# Найти оценки студентов в отдельной группе по определенному предмету.

from sqlalchemy import select, func

from connect_db import session
from models import Student, Faculty, Subject, Grade

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(
                Student.last_name,
                Student.first_name,
                Faculty.name,
                Subject.title,
                Grade.grade,
            )
            .select_from(Student)
            .join(Grade, Grade.student_id == Student.id)
            .join(Faculty, Student.faculty_id == Faculty.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(Faculty.id == 2)
            .filter(Subject.id == 1)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)

# SELECT s.last_name, s.first_name, f.name, title, m.mark
# FROM students AS s
#          INNER JOIN main.marks m on s.id = m.student_id
#          INNER JOIN main.faculties f on f.id = s.faculty_id
#          INNER JOIN main.subjects s2 on s2.id = m.subject_id
#          INNER JOIN main.marks m2 on s.id = m2.student_id
# WHERE f.name = '?'
#   AND title = '?';
