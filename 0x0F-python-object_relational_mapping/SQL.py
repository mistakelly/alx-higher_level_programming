from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory', echo=True)
print(engine)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class student_table(Base):
    pass