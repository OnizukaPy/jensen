from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os

PATH = '/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/Utveckling av webbapplikationer/Flask/Terzo tentativo'
DBNAME = 'tutorial.db'
SQLLITE = 'sqlite:///'+PATH+'/'+DBNAME
print(PATH+'/'+DBNAME)

engine = create_engine(SQLLITE, echo=True)
Base = declarative_base()

########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password

# create tables
Base.metadata.create_all(engine)