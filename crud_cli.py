import argparse

from models import Faculty
from connect_db import session

parser = argparse.ArgumentParser()

parser.add_argument(
    "-a",
    "--action",
    action="store",
    dest="action",
    choices=["create", "list", "update", "remove"],
)


parser.add_argument(
    "-m",
    "--model",
    action="store",
    dest="model",
    choices=["Faculty", "Student", "Subject", "Professor", "Grade"],
)

parser.add_argument("--id", action="store", dest="id", required=False)

parser.add_argument("-n", "--name", action="store", dest="name", required=False)

args = parser.parse_args()

model = args.model
name = args.name

faculty = Faculty(name=name)
session.add(faculty)
session.commit()
