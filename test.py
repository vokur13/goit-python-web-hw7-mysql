from decouple import config

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)

db_user = config("DATABASE_USER", default="root")
db_pass = config("DATABASE_PASSWORD", default="password")
db_host = config("DATABASE_HOST", default="localhost")
db_port = config("DATABASE_PORT", default="3306")

engine = create_engine(
    f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port}/test_db",
    echo=True,
)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(128)),
    Column("fullname", String(128)),
)

addresses = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("email_address", String(128), nullable=False),
)

if __name__ == "__main__":
    metadata.create_all(engine)
