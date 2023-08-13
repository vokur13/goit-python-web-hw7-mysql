# SELECT nt.id, nt.name, rc.description, rc.done, t.name as tag
# FROM notes AS nt
# LEFT JOIN records AS rc ON rc.note_id =  nt.id
# LEFT JOIN note_m2m_tag AS nmmt ON nmmt.note = nt.id
# LEFT JOIN tags AS t ON t.id = nmmt.tag
# WHERE t.name = 'food'


# from sqlalchemy import select
#
# from connect_db import session
# from models import Note, Tag, Record, note_m2m_tag
#
# if __name__ == '__main__':
#     q = session.execute(
#         select(Note.id, Note.name, Record.description, Record.done, Tag.name.label('tag'))
#         .join(Record)
#         .join(note_m2m_tag)
#         .join(Tag).filter(Tag.name == 'food')
#           ).mappings().all()
#
#     print(q)
