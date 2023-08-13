# Найти какие курсы читает определенный преподаватель.

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

# SELECT p.last_name, p.first_name, s.title
# FROM professors AS p
#          LEFT JOIN main.subjects s on p.id = s.professor_id WHERE p.id=1;
