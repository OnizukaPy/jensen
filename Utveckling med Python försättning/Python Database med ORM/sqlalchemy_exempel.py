from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import database_exists, create_database

# Create database

# Instansiera dbmoter
engine = create_engine('sqlite:///home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/Utveckling med Python försättning/Python Database med ORM/prova.db')

# instansiera Session
session = sessionmaker(bind=engine)

# Skapa tabeller med klass
Base = declarative_base()

class User(Base):

    __tablename__ = "user_account"

    id  = Column(Integer, primary_key=True)
    name  = Column(String)

    def __init__(self, name):
        self.name = name

