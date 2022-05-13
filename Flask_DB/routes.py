from flask import render_template, url_for, redirect, flash
from Flask_DB import app, db
from Flask_DB.forms import RegistrationForm, LoginForm
from Flask_DB.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    db.create_all()
    return render_template('home.html', title='Home', users=User.query.all())


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('login.html', title='Login', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Successfully Registered!, You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
