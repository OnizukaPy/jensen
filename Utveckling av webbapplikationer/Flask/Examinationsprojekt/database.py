from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import select

import os
import pandas as pd

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
    
# to find last_id in the table
def find_last_id(table):
    '''
    table = name of the table into the database
    '''
    stmt = select(table)
    i = 0
    for user in session.scalars(stmt):
        i += 1

    return i

##########
## Main ##
##########

# Database's data
db_namn = 'pizzeria.db'
path = 'Utveckling av webbapplikationer/Flask/Examinationsprojekt/'
print(delete_db(path, db_namn))

# Create engine
engine = create_engine('sqlite:///'+ path + db_namn)

# Create connection for quering
connection = engine.connect()

# Initiate session
session = sessionmaker(bind=engine)()
Base = declarative_base()

# Create Tables
class Users(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    mail = Column(String(255))
    password = Column(String(255))

    def __init__(self, id, name, mail, password):

        self.id = id
        self.name = name
        self.mail = mail
        self.password = password

class Admin(Base):

    __tablename__ = "Admin"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    mail = Column(String(255))
    password = Column(String(255))

    def __init__(self, id, name, mail, password):

        self.id = id
        self.name = name
        self.mail = mail
        self.password = password

class Pizzas(Base):
    
        __tablename__ = "Pizzas"
    
        id = Column(Integer, primary_key=True)
        name = Column(String(255))
        price = Column(String(255))
        size = Column(Integer)
        toppings = Column(String(255))
    
        def __init__(self, id, name, price, size, toppings):
    
            self.id = id
            self.name = name
            self.price = int(price)
            self.size = size
            self.toppings = toppings


# Create database with tables
Base.metadata.create_all(engine)

# to insert data value
def InsertPizza(table, name, price, size, toppings):
    '''
    table = name of the table into the database
    '''
    md = table(
        id=find_last_id(table)+1, 
        name=name,
        price=price,
        size=size,
        toppings=toppings
        )

    print(md)
    session.add_all([md])
    session.commit()

def DataFromKb(table, name, mail, password):
    '''
    table = name of the table into the database
    '''
    md = table(
        id=find_last_id(table)+1, 
        name=name,
        mail=mail, 
        password=password
        )

    print(md)
    session.add_all([md])
    session.commit()

# to insert administrator data value
DataFromKb(Admin, 'Ivan', 'admin@admin.it', 'Admin123')

# to insert first user data value
DataFromKb(Users, 'prova', 'prova@prova.it', 'prova')

# to insert pizza data value
df = pd.read_csv(path + 'pizzeria.csv')
for i in range(len(df)):
    InsertPizza(Pizzas, df['Name'][i], df['Price'][i], df['Size'][i], df['Toppings'][i])