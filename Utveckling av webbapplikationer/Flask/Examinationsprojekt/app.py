from flask import Flask, render_template, request, url_for   
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
import os

############################################################################
## Database creation                                                      ##
############################################################################

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
    

############################################################################
## Flask application                                                      ##
############################################################################

# Database's data
db_namn = 'pizzeria.db'
path = 'Utveckling av webbapplikationer/Flask/Examinationsprojekt/'
#print(delete_db(path, db_namn))

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{path}{db_namn}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)


db.session.add(
                db.Admin(
                    name='admin',
                    email='admin@admin.it',
                    password='admin'
                )
        )
db.session.add(
                db.Users(
                    name='prova',
                    email='prova@prova.it',
                    password='prova'
                )
        )

db.session.commit()

# create the routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    
    if request.method == "POST":
        user = db.User(
            email=request.form["email"],
            password=request.form["password"],
        )
        db.session.add(user)
        db.session.commit()

    return render_template('add_users.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        result_admin = db.session.query(db.Admin).all()
        result_users = db.session.query(db.User).all()
        mail_admin_list = []
        psw_admin_list = []
        name_admin_list = []
        for row in result_admin:
            name_admin_list.append(row.name)
            mail_admin_list.append(row.mail)
            psw_admin_list.append(row.password)
        
        mail_users_list = []
        psw_users_list = []
        name_users_list = []

        for row in result_users:
            name_users_list.append(row.name)
            mail_users_list.append(row.mail)
            psw_users_list.append(row.password)
        
        for i in range(len(mail_admin_list)):
            if email == mail_admin_list[i] and password == psw_admin_list[i]:
                name = name_admin_list[i]
                page = 'admin.html'
                return render_template(page, name=name)
                

            elif email == mail_users_list[i] and password == psw_users_list[i]:
                name = name_users_list[i]
                page = 'users.html'
                return render_template(page, name=name)
                
            else:
                render_template('login.html')
                break
        
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)