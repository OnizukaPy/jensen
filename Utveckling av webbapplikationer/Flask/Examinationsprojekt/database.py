from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os

PATH = '/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/Utveckling av webbapplikationer/Flask/Examinationsprojekt/'
DBNAME = 'pizzeria.db'
SQLLITE = 'sqlite:///'+PATH+DBNAME
print(PATH+DBNAME)

###############
## Functions ##
###############

# delete database
def delete_db(path, db_namn):
    '''
    db_namn = name of the database
    '''
    file_list = os.listdir(path)

    #for file in file_list:
    if db_namn in file_list:
        try:
            os.remove(path+db_namn)
        except OSError as e:
            return e
        else:
            return "File is deleted successfully"
    else:
        return "Database is not in the directory"


##########
## Main ##
##########

# Database's data
print(delete_db(PATH, DBNAME))

# Create engine
engine = create_engine(SQLLITE, echo=True)

# Create session
Base = declarative_base()

# Create Tables
class Users(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    mail = Column(String(255))
    password = Column(String(255))
    role = Column(String(255))

    def __init__(self, name, mail, password, role):

        self.name = name
        self.mail = mail
        self.password = password
        self.role=role
class Pizzas(Base):

        __tablename__ = "Pizzas"

        id = Column(Integer, primary_key=True)
        name = Column(String(255))
        price = Column(String(255))
        size = Column(Integer)
        toppings = Column(String(255))

        def __init__(self, name, price, size, toppings):

            self.name = name
            self.price = int(price)
            self.size = size
            self.toppings = toppings


# Create database with tables
Base.metadata.create_all(engine)
