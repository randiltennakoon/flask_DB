from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '225dccaa4ab7a419f983d2f24821fc93'



@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)



if __name__ == '__main__':
    app.run(debug=True)