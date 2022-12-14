## Folder link om GitHub: 
# https://github.com/OnizukaPy/jensen/tree/main/Utveckling%20med%20Python%20f%C3%B6rs%C3%A4ttning/inl%C3%A4mninguppgifter
## Faker documentation:
# https://faker.readthedocs.io/en/master/ 


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import select

from faker import Faker
from random import choice
import os

import PySimpleGUI as sg

#---------------------------
# FUNCTIONS
#---------------------------

# to insert data value
def insert_data_from_keyboard(table):
    '''
    table = name of the table into the database
    '''
    md = table(
        id=find_last_id(table)+1, 
        namn=input('Namn: '), 
        efternamn=input('Efternamn: '),
        medlemsnummer=input('PN: '), 
        gatuadress=input('Gatuadress: '), 
        postnummer=int(input('Postnummer: ')), 
        postadress=int(input('Postadress: ')),
        ort=input('Ort: '),
        avgift=input('Avgift Y/N: ')
        )

    print(md)
    session.add_all([md])
    session.commit()

# to insert random values
def insert_random(table, last_id, n):
    '''
    table = name of the table in the database
    last_id = the last number av id in the table
    n = number av medlem to add
    '''
    fake = Faker('sv_SE')
    first = last_id + 1 
    last = first + n

    for i in range(first, last):

        temp = fake.address().split()

        md = table(
                id=i, 
                namn=fake.first_name(), 
                efternamn=fake.last_name(), 
                medlemsnummer=fake.ssn(), 
                gatuadress=temp[0], 
                postnummer=temp[1], 
                postadress=temp[2],
                ort=temp[3],
                avgift=choice(['Y', 'N'])
                )

        print(md)
        session.add_all([md])
        session.commit()

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

# delete database
def delete_db(db_namn):
    '''
    db_namn = name of the database
    '''
    file_list = os.listdir('.')

    #for file in file_list:
    if db_namn in file_list:
        try:
            os.remove(db_namn)
        except OSError as e:
            print(e)
        else:
            print("File is deleted successfully")
    else:
        print("Database is not in the directory")

# To delete data
def delete_from_db(table, id):
    '''
    table = name of the table in the database
    id = the row's id to cancel
    '''
    temp = session.get(table, id)
    session.delete(temp)
    session.commit()

# To show rows from db
def show_row_from_db(table):
    '''
    table = name of the table in the database
    '''
    db = select(table)
    for row in session.scalars(db):
        print(row)

# To insert data with a simple user interface
def insert_data_from_interface(table):
    '''
    table = name of the table in the database
    '''
    sg.theme('Topanga')      

    layout = [
        [sg.Text('Please enter data into the table')],        
        [sg.Text('Namn', size=(15, 1)), sg.InputText()],            
        [sg.Text('Efternamn', size=(15, 1)), sg.InputText()],         
        [sg.Text('Medlemsnummer', size=(15, 1)), sg.InputText()], 
        [sg.Text('Gatuadress', size=(15, 1)), sg.InputText()],
        [sg.Text('Postnummer', size=(15, 1)), sg.InputText()],
        [sg.Text('Postadress', size=(15, 1)), sg.InputText()],
        [sg.Text('Ort', size=(15, 1)), sg.InputText()],  
        [sg.Text('Avgift Y/N', size=(15, 1)), sg.InputText()],   
        [sg.Submit(), sg.Cancel()]                                  
    ]

    window = sg.Window('Simple data entry window', layout)
    while True:

        event, values = window.read()
        
        if event == 'Cancel' or event == sg.WIN_CLOSED: 
            print('You have not insert data into the table')
            break
        else:
            md = table(
                id=find_last_id(Medlem)+1, 
                namn=values[0], 
                efternamn=values[1],
                medlemsnummer=values[2], 
                gatuadress=values[3], 
                postnummer=int(values[4]), 
                postadress=int(values[5]),
                ort=values[6],
                avgift=values[7]
                )

            print(md)
            session.add_all([md])
            session.commit()

    window.close()

#---------------------------
# SQL 
#---------------------------

# Database's data

db_namn = 'Medlemsregister.db'

# Create database
engine = create_engine('sqlite:///Utveckling med Python försättning/inlämninguppgifter/'+db_namn)

session = sessionmaker(bind=engine)()
Base = declarative_base()

# Create Tables
class Medlem(Base):

    __tablename__ = "Medlem"

    id = Column(Integer, primary_key=True)
    namn = Column(String(255))
    efternamn = Column(String(255))
    medlemsnummer = Column(Integer)
    gatuadress = Column(String(255))
    postnummer = Column(Integer)
    postadress = Column(Integer)
    ort = Column(String(255))

    def __init__(self, id, namn, efternamn, medlemsnummer, gatuadress, postnummer, postadress, ort):

        self.id = id
        self.namn = namn
        self.efternamn = efternamn
        self.medlemsnummer = medlemsnummer
        self.gatuadress = gatuadress
        self.postnummer = postnummer
        self.postadress = postadress
        self.ort = ort
    
    def __repr__(self) -> str:
        return f"Medlem({self.id!r}, {self.namn!r}, {self.efternamn!r},{self.medlemsnummer!r}, {self.gatuadress!r} {self.postnummer!r} {self.ort!r}, Betalt avgift? {self.avgift!r})"

Base.metadata.create_all(engine)

#---------------------------
# SCRIPT
#---------------------------

# Insert random data
insert_random(Medlem, 0, 100)

# Insert data in the table
insert_data_from_keyboard(Medlem)

# Use grafic interface for insert data
insert_data_from_interface(Medlem)

# Show table's data
show_row_from_db(Medlem)

# Delete last row into the table 
delete_from_db(Medlem, find_last_id(Medlem))

# Delete DB
delete_db(db_namn)




