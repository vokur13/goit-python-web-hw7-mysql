# Найти средний балл, который ставит определенный преподаватель по своим предметам.

from sqlalchemy import select, func

from connect_db import session
from models import Professor, Subject, Grade

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(
                Professor.last_name,
                Professor.first_name,
                Subject.title,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .select_from(Professor)
            .join(Subject, Professor.id == Subject.professor_id)
            .join(Grade, Subject.id == Grade.subject_id)
            .group_by(Professor.last_name, Professor.first_name, Subject.title)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)

# SELECT p.last_name, p.first_name, round(AVG(m.mark), 2)
# FROM professors p
#          INNER JOIN main.subjects s on p.id = s.professor_id
#          INNER JOIN main.marks m on s.id = m.subject_id
# GROUP BY p.last_name, p.first_name;
