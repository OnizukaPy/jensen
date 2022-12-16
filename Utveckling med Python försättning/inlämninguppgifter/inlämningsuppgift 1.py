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
# FUNCTIONS - SQL
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
    temp = ''
    for row in session.scalars(db):
        temp = temp + str(row) + '\n'
    
    if temp == '':
        return 'No results'
    else:
        return temp


# To do query into the database attribut namn
def query_in_db(table, sql_query):
    '''
    table = name of the table in the database
    sql_query = the query to search
    '''
    query = select([table]).where(table.namn.in_([sql_query]))
    temp = ''
    for row in session.scalars(query):
        temp = temp + str(row) + '\n'
    
    if temp == '':
        return 'No results'
    else:
        return temp

#---------------------------
# FUNCTIONS - SIMPLEGUI
#---------------------------

# Window´s functions

# Clear
def clear(window):
    window['-NN-'].update('')
    window['-EFNN-'].update('')
    window['-MEDN-'].update('')
    window['-GA-'].update('')
    window['-POSTN-'].update('')
    window['-POSTA-'].update('')
    window['-ORT-'].update('')
    window['-AVG-'].update('')

# Send
def send_data_to_database(table, values):
        md = table(
            id=find_last_id(table)+1, 
            namn=values['-NN-'], 
            efternamn=values['-EFNN-'],
            medlemsnummer=values['-MEDN-'], 
            gatuadress=values['-GA-'], 
            postnummer=int(values['-POSTN-']), 
            postadress=int(values['-POSTA-']),
            ort=values['-ORT-'],
            avgift=values['-AVG-']
            )

        print(md)
        print(values)
        session.add_all([md])
        session.commit()

# To insert data with a simple user interface
def insert_data_from_interface(table):
    '''
    table = name of the table in the database
    '''
    sg.theme('Topanga')      

    layout = [
        [sg.Text('Please enter data into the table')],        
        [sg.Text('Namn', size=(15, 1)), sg.InputText(key='-NN-')],            
        [sg.Text('Efternamn', size=(15, 1)), sg.InputText(key='-EFNN-')],         
        [sg.Text('Medlemsnummer', size=(15, 1)), sg.InputText(key='-MEDN-')], 
        [sg.Text('Gatuadress', size=(15, 1)), sg.InputText(key='-GA-')],
        [sg.Text('Postnummer', size=(15, 1)), sg.InputText(key='-POSTN-')],
        [sg.Text('Postadress', size=(15, 1)), sg.InputText(key='-POSTA-')],
        [sg.Text('Ort', size=(15, 1)), sg.InputText(key='-ORT-')],  
        [sg.Text('Avgift Y/N', size=(15, 1)), sg.InputText(key='-AVG-')],  
        #[sg.In(key='-IN-')], 
        #[sg.Output(size=(50,10), key='-OUTPUT-')],
        [sg.Button('Save and exit'), sg.Cancel(), sg.Button('Save and continue'), sg.Button('Clear'), sg.Button('Random')]                                  
    ]

    window = sg.Window('Simple data entry window', layout)
    while True:

        event, values = window.read()
        
        if event == 'Cancel' or event == sg.WIN_CLOSED: 
            print('You have not insert data into the table')
            break
        elif event == 'Clear':
            clear(window)

        elif event == 'Save and continue':
            send_data_to_database(table, values)
            clear(window)

        elif event == 'Random':
            insert_random(table, find_last_id(table), 10)

        else:
            send_data_to_database(table, values)
            break

        
    window.close()

# To delete roe into the table
def delete_from_db_with_interface(table):
    '''
    table = name of the table in the database
    '''
    sg.theme('Topanga')
    layout = [
        [sg.Text('Please enter id')],        
        [sg.Text('id', size=(15, 1)), sg.InputText(key='-ID-')],
        [sg.Button('Ok'), sg.Cancel(), sg.Button('Last Row'), sg.Button('Clear')]                                  
    ]

    window = sg.Window('Delete row from database with id', layout)
    while True:

        event, values = window.read()

        if event == 'Cancel' or event == sg.WIN_CLOSED: 
            break
        elif event == 'Last Row':
            delete_from_db(table, find_last_id(table))
            break
        elif event == 'Ok':
            delete_from_db(table, values['-ID-'])
            break
        elif event == 'Clear':
            window['-ID-'].update('')
        
    window.close()

def query(table):
    '''
    table = name of the table in the database
    '''
    layout = [
        [sg.Text("Query: "), sg.Input(key='-QUERY-')],
        [sg.Ok(), sg.Button('Show')],
        [sg.Text("", key='OUTPUT')]
    ]

    window = sg.Window("Just a window", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Ok':
            name = values['-QUERY-']
            temp = query_in_db(table, name)
            window['OUTPUT'].update(value=temp)
        elif event == 'Show':
            name = show_row_from_db(table)
            window['OUTPUT'].update(value=name)

    window.close()

#---------------------------
# SCRIPT - SQL 
#---------------------------

# Database's data
db_namn = 'Medlemsregister.db'
path = '/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/Utveckling med Python försättning/inlämninguppgifter/'
print(delete_db(path, db_namn))

# Create engine
engine = create_engine('sqlite:///Utveckling med Python försättning/inlämninguppgifter/'+db_namn)

# Create connection for quering
connection = engine.connect()

# Initiate session

session = sessionmaker(bind=engine)()
Base = declarative_base()

# Create Tables
class Medlem(Base):

    __tablename__ = "Medlem"

    id = Column(Integer, primary_key=True)
    namn = Column(String(255))
    efternamn = Column(String(255))
    medlemsnummer = Column(String(255))
    gatuadress = Column(String(255))
    postnummer = Column(Integer)
    postadress = Column(Integer)
    ort = Column(String(255))
    avgift = Column(String(1))

    def __init__(self, id, namn, efternamn, medlemsnummer, gatuadress, postnummer, postadress, ort, avgift):

        self.id = id
        self.namn = namn
        self.efternamn = efternamn
        self.medlemsnummer = medlemsnummer
        self.gatuadress = gatuadress
        self.postnummer = postnummer
        self.postadress = postadress
        self.ort = ort
        self.avgift = avgift

    def __repr__(self) -> str:
        return f"Medlem({self.id!r}, {self.namn!r}, {self.efternamn!r},{self.medlemsnummer!r}, {self.gatuadress!r} {self.postnummer!r} {self.ort!r}, Betalt avgift? {self.avgift!r})"

# Create database with tables
Base.metadata.create_all(engine)

#---------------------------
# SCRIPT
#---------------------------

# Main window
sg.theme('Topanga')
layout = [
    [sg.Button('Insert data'), sg.Button('Delete data'), sg.Button('Do a query')],
    #[sg.Button('Delete database')],
    [sg.Text("", key='OUTPUT')],
    [sg.Button('Cancel')]
    ]

window = sg.Window('Simple window', layout)

while True:

    event, values = window.read()
    if event == 'Delete database':
        text = delete_db(path, db_namn)
        window['OUTPUT'].update(value=text)
    elif event == 'Insert data':
        insert_data_from_interface(Medlem)
    
    elif event == 'Delete data':
        delete_from_db_with_interface(Medlem)

    elif event == 'Do a query':
        query(Medlem)
    
    elif event == 'Cancel' or event == sg.WIN_CLOSED:
        break

window.close()

'''
# Insert random data
insert_random(Medlem, 0, 100)

# Insert data in the table
insert_data_from_keyboard(Medlem)

# Use grafic interface for insert data
insert_data_from_interface(Medlem)

# Use grafic interface for delete data
delete_from_db_with_interface(Medlem)

# Search into the database with interface
query_in_db(Medlem)

# Show table's data
show_row_from_db(Medlem)

# Delete last row into the table 
delete_from_db(Medlem, find_last_id(Medlem))

# Delete DB
delete_db(db_namn)
'''



