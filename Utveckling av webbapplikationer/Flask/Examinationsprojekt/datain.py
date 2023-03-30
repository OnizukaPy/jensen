import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import *
import pandas as pd

# to insert data value
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

# to insert data value
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

engine = create_engine(SQLLITE, echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# to insert administrator data value
DataFromKb(Users, 'Ivan', 'ivan@ivan.it', 'Ivan123', 'admin')

# to insert pizza data value
df = pd.read_csv(PATH + 'pizzeria.csv')
for i in range(len(df)):
    InsertPizza(Pizzas, df['Name'][i], df['Price'][i], df['Size'][i], df['Toppings'][i])

# commit the record the database
#session.commit()