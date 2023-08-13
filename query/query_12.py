# -- Оценки студентов в определенной группе по определенному предмету на последнем занятии.


from sqlalchemy import select, func

from connect_db import session
from models import Student, Faculty, Subject, Grade

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(
                Student.last_name.label("student_last_name"),
                Student.first_name.label("student_first_name"),
                Faculty.name.label("faculty_name"),
                Subject.title.label("subject_title"),
                Grade.grade.label("grade"),
                func.max(Grade.date_of),
            )
            .select_from(Grade)
            .join(Subject, Subject.id == Grade.subject_id)
            .join(Student, Student.id == Grade.student_id)
            .join(Faculty, Faculty.id == Student.faculty_id)
            .filter(Faculty.id == 1)
            .filter(Subject.id == 1)
            .group_by(
                "student_last_name",
                "student_first_name",
                "faculty_name",
                "subject_title",
                "grade",
            )
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)


# SELECT s1.last_name, s1.first_name, f.name, s.title, m.mark, max(m.date_of)
# FROM marks m
#          INNER JOIN main.subjects s on s.id = m.subject_id
#          INNER JOIN main.students s1 on s1.id = m.student_id
#          INNER JOIN main.faculties f on f.id = s1.faculty_id
# WHERE f.name = '?'
#   AND s.title = '?';
