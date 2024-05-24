# This app.py is the 'controller' it links the View to the Models.
'''
The Flask Application instance needs to know what code it needs to run for 
each URL requested, so it keeps mapping (ORM) of URLs to Python functions. 
The association between a URL and the function that handles it is called 
a route.
'''

from flask import Flask, render_template, url_for, flash, redirect
from flask_app.forms.forms import LoginForm, createAccount
from flask_bootstrap import Bootstrap
from flask_app.models import db, User

# Layout for the page, (View) where Jinja Template is.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

# Create tables in the database
with app.app_context():
    db.create_all()

@app.route('/content')
def content():
    return render_template('content.html')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/rest')
def rest():
    return render_template('rest.html')

@app.route('/javascript')
def javascript():
    return render_template('javascript.html')

@app.route('/agileprocesses')
def agileprocesses():
    return render_template('agileprocesses.html')

@app.route('/databases')
def databases():
    return render_template('databases.html')


@app.route('/flaskInfo')
def flaskInfo():
    return render_template('flaskInfo.html')

@app.route('/labs')
def labs():
    return render_template('labs.html')

@app.route('/testing')
def testing():
    return render_template('testing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = createAccount()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)




