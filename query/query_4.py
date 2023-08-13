# -- Найти средний балл на потоке (по всей таблице оценок).

from sqlalchemy import select, func

from connect_db import session
from models import Grade

if __name__ == "__main__":
    stmt = (
        (
            session.execute(
                select(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
            )
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)

# SELECT round(AVG(m.mark), 2)
# FROM marks AS m;
