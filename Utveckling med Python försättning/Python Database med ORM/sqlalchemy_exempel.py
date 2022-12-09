from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import database_exists, create_database

# Create database

engine = create_engine('sqlite:///ivan.db')

session = sessionmaker(bind=engine)()
Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, id, name):

        self.id = id
        self.name = name

Base.metadata.create_all(engine)