## tutorial used: https://pythonspot.com/login-authentication-with-flask/
## template used: https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_gourmet_catering&stacked=h

# Import libraries and modules needed for the program
# importing of flask to create the web application
from flask import Flask, flash, redirect, render_template, request, session, abort

# importing of sqlalchemy to read and modify the database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from sqlalchemy import select

# importing of the database and functions from the database.py file
from database import *

# importing tables from the database
import datain  

engine = create_engine(SQLLITE, echo=True)
app = Flask(__name__)

#################
### Functions ###
#################

# function to list the pizzas in the database and return a list with the pizzas
def list_pizza():
    Session = sessionmaker(bind=engine)
    s = Session()
    result_pizzas = s.query(Pizzas).all()
    name_pizzas = []
    price_pizzas = []
    size_pizzas = []
    toppings_pizzas = []
    id_pizzas = []
    for row in result_pizzas:
        name_pizzas.append(row.name)
        price_pizzas.append(row.price)
        size_pizzas.append(row.size)
        toppings_pizzas.append(row.toppings)
        id_pizzas.append(row.id)
    list_pizzas = []
    for i in range(len(name_pizzas)):
        list_pizzas.append([name_pizzas[i], price_pizzas[i], size_pizzas[i], toppings_pizzas[i], id_pizzas[i]])
    return list_pizzas

# function to list the users in the database and return a list with the users
def list_user():
    Session = sessionmaker(bind=engine)
    s = Session()
    result_users = s.query(Users).all()
    name_users = []
    mail_users = []
    role_users = []
 
    for row in result_users:
        name_users.append(row.name)
        mail_users.append(row.mail)
        role_users.append(row.role)
        
    list_users = []
    for i in range(len(name_users)):
        list_users.append([name_users[i], mail_users[i], role_users[i]])
    return list_users

#################
### Routes ######
#################

# route to the index page
@app.route('/')
def index():

    list_pizzas = list_pizza()
    return render_template('index.html', pizzas=list_pizzas)

# route to the login and logout page
@app.route('/home')
def home(msg=''):
    if not session.get('logged_in'):
        return render_template('login.html', msg=msg)
    else:
        return render_template('logout.html', msg=msg)
    
# route to the sign up page
@app.route('/sign_up')
def sign_up():
    return render_template('register.html')

# route to the login page and check if the user is in the database
@app.route('/login', methods=['POST'])
def do_admin_login():
    msg = ''
    POST_EMAIL = str(request.form['email'])
    POST_PASSWORD = str(request.form['password'])
    POST_ROLE = str(request.form['role'])
    Session = sessionmaker(bind=engine)
    s = Session()
    
    query = s.query(Users).filter(Users.mail.in_([POST_EMAIL]), Users.password.in_([POST_PASSWORD]), Users.role.in_([POST_ROLE]))
    result = query.first()
    
    if result:
        session['logged_in'] = True
        if POST_ROLE == 'admin':
            msg = 'You are logged in as Admin'
            return render_template('admin.html', msg=msg, pizzas=list_pizza(), users=list_user())
        else:
            msg = 'You are logged in as costumer'
            return home(msg)
    else:
        msg = 'Login Error'
    return home(msg)

# route to the register page
@app.route('/register', methods=['POST'])
def do_registration():
    msg = ''
    POST_NAME = str(request.form['name'])
    POST_EMAIL = str(request.form['email'])
    POST_PASSWORD = str(request.form['password'])

    # check if the user already exists
    Session = sessionmaker(bind=engine)
    s = Session()
    # check if the email already exists using the exists() and the scalar() functions
    exists_criteria = exists().where(Users.mail==POST_EMAIL)    
    result = s.query(exists_criteria).scalar()      # returns True or False
    
    if result:
        msg = 'Account already exists'
        return render_template('register.html', msg=msg)
    else:
        datain.DataFromKb(Users, POST_NAME, POST_EMAIL, POST_PASSWORD, 'user')
        msg = 'You are registered'
    
    return home(msg)

# route to the logout page
@app.route("/logout")
def logout():
    session['logged_in'] = False
    msg = 'You are logged out'
    return home(msg)

# route to order menu page
@app.route('/order_menu')
def order_menu():
    if not session.get('logged_in'):
        msg = 'You are not logged in'
        return render_template('login.html', msg=msg)
    else:
        list_pizzas = list_pizza()
        return render_template('order_menu.html', pizzas=list_pizzas)

# route to order menu page
@app.route('/order', methods=['POST'])
def order():
    pizza = str(request.form['pizza'])
    quantity = str(request.form['quantity'])
    return render_template('confirm_order.html', pizza=pizza, quantity=quantity)

# route to add pizzas
@app.route('/add_pizza', methods=['POST'])
def add_pizza():
    POST_PIZZA_NAME = str(request.form['name'])
    POST_PIZZA_PRICE = int(request.form['price'])
    POST_PIZZA_SIZE = str(request.form['size'])
    POST_PIZZA_TOPPINGS = str(request.form['toppings'])
    datain.InsertPizza(Pizzas, POST_PIZZA_NAME, POST_PIZZA_PRICE, POST_PIZZA_SIZE, POST_PIZZA_TOPPINGS)

    return render_template('admin.html', pizzas=list_pizza(), users=list_user())

# route to deleting pizzas
@app.route('/delete_pizza', methods=['POST'])
def delete_pizza():
    POST_PIZZA_ID = int(request.form['id'])
    datain.DeletePizza(Pizzas, POST_PIZZA_ID)

    return render_template('admin.html', pizzas=list_pizza(), users=list_user())

# route to mofiy pizzas
@app.route('/modify_pizza', methods=['POST'])
def modify_pizza():
    POST_PIZZA_ID = int(request.form['id'])
    POST_PIZZA_NAME = str(request.form['name'])
    POST_PIZZA_PRICE = int(request.form['price'])
    POST_PIZZA_SIZE = str(request.form['size'])
    POST_PIZZA_TOPPINGS = str(request.form['toppings'])
    datain.UpdatePizza(Pizzas, POST_PIZZA_ID, POST_PIZZA_NAME, POST_PIZZA_PRICE, POST_PIZZA_SIZE, POST_PIZZA_TOPPINGS)

    return render_template('admin.html', pizzas=list_pizza(), users=list_user())



# loop to run the application
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)