from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = '225dccaa4ab7a419f983d2f24821fc93'



@app.route('/')
def home():
    return render_template('home.html', title='Home')



if __name__ == '__main__':
    app.run(debug=True)