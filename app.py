from flask import Flask, render_template, url_for, redirect, flash, request
from forms import RegistrationForm, LoginForm
# from models import User
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '225dccaa4ab7a419f983d2f24821fc93'


# database creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}'"



@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated():
    #     return redirect(url_for('home'))

    form = LoginForm()
    # if request.method == 'POST':
    #     flash('Login successful', 'success')
    #     return redirect(url_for('home'))
    # else:
    #     flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # if form.validate_on_submit():
    #     print('done')
        # username = form.username.data 
        # email = form.email.data 
        # password = form.password.data

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        #db.create_all()
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash(f'User {username} successfully registered using the email {email}!, Please log in to continue.', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', title='Register', form=form)



if __name__ == '__main__':
    app.run(debug=True)