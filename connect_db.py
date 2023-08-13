from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/university")
Session = sessionmaker(bind=engine)
session = Session()
