# -- Средний балл, который определенный преподаватель ставит определенному студенту.


from sqlalchemy import select, func

from connect_db import session
from models import Student, Professor, Subject, Grade

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(
                Professor.last_name.label("professor_last_name"),
                Professor.first_name.label("professor_first_name"),
                Student.last_name.label("student_last_name"),
                Student.first_name.label("student_first_name"),
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .select_from(Grade)
            .join(Subject, Subject.id == Grade.subject_id)
            .join(Professor, Professor.id == Subject.professor_id)
            .join(Student, Student.id == Grade.student_id)
            .filter(Professor.id == 1)
            .filter(Student.id == 1)
            # .group_by(Student.last_name, Student.first_name, Subject.title)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)


# SELECT s2.last_name, s2.first_name, p.last_name, p.first_name, round(AVG(m.mark), 2)
# FROM marks m
#          INNER JOIN main.subjects s on s.id = m.subject_id
#          INNER JOIN main.professors p on p.id = s.professor_id
#          INNER JOIN main.students s2 on s2.id = m.student_id
# WHERE s2.last_name = '?'
#   AND p.last_name = '?';
