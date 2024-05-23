# This app.py is the 'controller' it links the View to the Models.
'''
The Flask Application instance needs to know what code it needs to run for 
each URL requested, so it keeps mapping (ORM) of URLs to Python functions. 
The association between a URL and the function that handles it is called 
a route.
'''

from flask import Flask, render_template, url_for

# Layout for the page, (View) where Jinja Template is.
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)




