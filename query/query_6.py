# Найти список студентов в определенной группе.

from sqlalchemy import select, func

from connect_db import session
from models import Professor, Subject

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(Professor.last_name, Professor.first_name, Subject.title)
            .select_from(Professor)
            .join(Subject)
            .filter(Professor.id == 1)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)

# SELECT f.name, s.last_name, s.first_name
# FROM faculties AS f
#          LEFT JOIN main.students s on f.id = s.faculty_id
# WHERE f.name = 'Illustrator';
