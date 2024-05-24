# This app.py is the 'controller' it links the View to the Models.
'''
The Flask Application instance needs to know what code it needs to run for 
each URL requested, so it keeps mapping (ORM) of URLs to Python functions. 
The association between a URL and the function that handles it is called 
a route.
'''

from flask import Flask, render_template, url_for
from flask_app.forms.forms import LoginForm
from flask_bootstrap import Bootstrap

# Layout for the page, (View) where Jinja Template is.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for CSRF protection
Bootstrap(app)

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
    form = LoginForm()  # Create an instance of the LoginForm class
    if form.validate_on_submit():  # If the form is submitted and valid
        # Flash a success message
        flash(f'Login requested for user {form.username.data}', 'success')
        # Redirect the user to the home page
        return redirect(url_for('home'))
    # Render the login page template and pass the form to it
    return render_template('login.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)




