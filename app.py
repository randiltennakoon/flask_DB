from flask import Flask, render_template, url_for, redirect, flash, request
# from forms import RegistrationForm, LoginForm
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



@app.route('/')
def home():
    db.create_all()
    return render_template('home.html', title='Home', users=User.query.all())


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user:
            if password != user.password:
                flash(f"Username or Password is not correct!", 'danger')
                return render_template('login.html', title='Login')
            else:
                flash(f"Successfully Logged In!", 'success')
                return redirect(url_for('home'))
    else:
        return render_template('login.html', title='Login')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash(f"Successfully Registered!", 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', title='Register')



if __name__ == '__main__':
    app.run(debug=True)