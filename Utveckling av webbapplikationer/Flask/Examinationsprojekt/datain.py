# import the necessary libraries and modules needed for the program
# importing of sqlalchemy to read and modify the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# importing of the database and functions from the database.py file
from database import *

# importing of pandas to read the csv file
import pandas as pd

#################
### Functions ###
#################

# function to insert userdata into the database
def DataFromKb(table, name, mail, password, role):
    '''
    table = name of the table into the database
    '''
    md = table(
        name=name,
        mail=mail, 
        password=password,
        role=role
        )

    print(md)
    session.add_all([md])
    session.commit()

# function to insert data of pizzas into the database
def InsertPizza(table, name, price, size, toppings):
    '''
    table = name of the table into the database
    '''
    md = table(
        name=name,
        price=price,
        size=size,
        toppings=toppings
        )

    print(md)
    session.add_all([md])
    session.commit()

# fuction to delete pizza from the database
def DeletePizza(table, id):
    '''
    table = name of the table into the database
    id = id of the pizza to delete
    '''
    session.query(table).filter(table.id == id).delete()
    session.commit()

# function to update pizza in the database
def UpdatePizza(table, id, name=None, price=None, size=None, toppings=None):
    '''
    table = name of the table into the database
    id = id of the pizza to update
    '''
    session.query(table).filter(table.id == id).update({table.name: name, table.price: price, table.size: size, table.toppings: toppings})
    session.commit()


#################
### Main      ###
#################

# create the engine to connect to the database
engine = create_engine(SQLLITE, echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# insert data of admin user into the database
DataFromKb(Users, 'Ivan', 'ivan@ivan.it', 'Ivan123', 'admin')

# insert data of pizzas into the database
df = pd.read_csv(PATH + 'pizzeria.csv')
for i in range(len(df)):
    InsertPizza(Pizzas, df['Name'][i], df['Price'][i], df['Size'][i], df['Toppings'][i])
