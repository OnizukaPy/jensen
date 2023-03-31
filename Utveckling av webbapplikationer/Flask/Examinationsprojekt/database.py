# import libraries and modules needed for the program 
# importing of sqlalchemy to create a database

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# importing of os to create a path to the database
import os

# creating a path to the database
PATH = os.path.abspath(os.path.dirname(__file__)) + '/'

# creating a name for the database
DBNAME = 'pizzeria.db'

# creating a sqlpath to the database
SQLLITE = 'sqlite:///'+PATH+DBNAME

# printing the path to the database to check if the path is correct
print(PATH+DBNAME)

###############
## Functions ##
###############

# this function deletes the database if it is in the directory
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

# check if database is in the directory and delete it
print(delete_db(PATH, DBNAME))

# start the database creation
engine = create_engine(SQLLITE, echo=True)      # Create engine
Base = declarative_base()                       # Create declarative base

# Create Tables in the database
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
