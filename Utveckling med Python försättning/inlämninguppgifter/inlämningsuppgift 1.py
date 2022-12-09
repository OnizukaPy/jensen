## Folder link om GitHub: 
# https://github.com/OnizukaPy/jensen/tree/main/Utveckling%20med%20Python%20f%C3%B6rs%C3%A4ttning/inl%C3%A4mninguppgifter

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# Create database

engine = create_engine('sqlite:///Medlemsregister.db')

session = sessionmaker(bind=engine)()
Base = declarative_base()

class Medlem(Base):

    __tablename__ = "Medlem"

    id = Column(Integer, primary_key=True)
    namn = Column(String(255))
    efternamn = Column(String(255))
    medlemsnummer = Column(Integer)
    gatuadress = Column(String(255))
    postnummer = Column(Integer)
    postadress = Column(Integer)

    def __init__(self, id, name):

        self.id = id
        self.name = name

Base.metadata.create_all(engine)