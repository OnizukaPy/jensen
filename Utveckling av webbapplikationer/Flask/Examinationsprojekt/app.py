from flask import Flask, render_template, request, url_for  
from werkzeug.utils import secure_filename   
import database as db
import os      

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        db.DataFromKb(db.Users, name, email, password)
        return render_template('add_users.html')
    return render_template('add_users.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result_admin = db.session.query(db.Admin).all()
        result_users = db.session.query(db.Users).all()
        
        for row in result_admin:
            if row.mail == email and row.password == password:
                name = row.name
                page = 'admin.html'
                break 
        
        for row in result_users:
            if row.mail == email and row.password == password:
                name = row.name
                page = 'users.html'
                break

        return render_template(page, name=name)
                
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


#db.DataFromKb(db.Users)