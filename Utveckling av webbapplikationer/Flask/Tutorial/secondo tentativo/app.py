### https://www.youtube.com/watch?v=CQDh60KvziE 

from flask import Flask, render_template, request, url_for, redirect
from forms import RegistrationForm, LoginForm 

from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import database as db

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY']='key'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = generate_password_hash(form.password.data, method='sha256')

        try:
            new_user = db.Users(public_id=str(uuid.uuid4()), name=form.username.data, password=hashed_password, admin=False)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

        except:
            return redirect(url_for('index'))
        
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('menu'))
    form = LoginForm(request.form)
    return render_template('login.html', title='Login', form=form)

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html', title='Menu')


if __name__ == '__main__':
    app.run(debug=True)