## tutorial used: https://pythonspot.com/login-authentication-with-flask/
## template used: https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_gourmet_catering&stacked=h

# Import libraries and modules needed for the program
# importing of flask to create the web application
from flask import Flask, flash, redirect, render_template, request, session, abort

# importing of sqlalchemy to read and modify the database
from sqlalchemy.orm import sessionmaker

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
    for row in result_pizzas:
        name_pizzas.append(row.name)
        price_pizzas.append(row.price)
        size_pizzas.append(row.size)
        toppings_pizzas.append(row.toppings)
    list_pizzas = []
    for i in range(len(name_pizzas)):
        list_pizzas.append([name_pizzas[i], price_pizzas[i], size_pizzas[i], toppings_pizzas[i]])
    return list_pizzas

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

# route to the login page and check if the user is in the database
@app.route('/login', methods=['POST'])
def do_admin_login():
    msg = ''
    POST_EMAIL = str(request.form['email'])
    POST_PASSWORD = str(request.form['password'])
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Users).filter(Users.mail.in_([POST_EMAIL]), Users.password.in_([POST_PASSWORD]) )
    result = query.first()
    
    if result:
        session['logged_in'] = True
    else:
        msg = 'Login Error'
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

# loop to run the application
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

"""
@app.route('/')
def index():
    
    result_pizzas = session.query(Pizzas).all()
    name_pizzas = []
    price_pizzas = []
    size_pizzas = []
    toppings_pizzas = []
    for row in result_pizzas:
        name_pizzas.append(row.name)
        price_pizzas.append(row.price)
        size_pizzas.append(row.size)
        toppings_pizzas.append(row.toppings)
    list_pizzas = []
    for i in range(len(name_pizzas)):
        list_pizzas.append([name_pizzas[i], price_pizzas[i], size_pizzas[i], toppings_pizzas[i]])
    
    return render_template('index.html', pizzas=list_pizzas)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result_admin = db.session.query(db.Admin).all()
        result_users = db.session.query(db.Users).all()

        name_users = []
        mail_users = []
        password_users = []
        for row in result_users:
            name_users.append(row.name)
            mail_users.append(row.mail)
            password_users.append(row.password)

        name_admin = []
        mail_admin = []
        password_admin = []
        for row in result_admin:
            name_admin.append(row.name)
            mail_admin.append(row.mail)
            password_admin.append(row.password)

        if email in mail_admin and password in password_admin:
            msg = name_admin[mail_admin.index(email)]
            page = 'admin.html'
            
        elif email in mail_users and password in password_users:
            msg = name_users[mail_users.index(email)]
            page = 'users.html'
            
        else:
            msg = 'Login Error'
            page = 'login.html'
        
        return render_template(page, msg=msg)

    return render_template('login.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        db.DataFromKb(db.Users, name, email, password)
        return render_template('add_users.html', msg='User added')
    return render_template('add_users.html', msg='')

if __name__ == '__main__':
    app.run(debug=True)
"""