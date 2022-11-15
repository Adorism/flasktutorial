# This file can be called anything except for flask.py which woulr result in conflict
# Run this file using either flask command or python -m flask and tell where application is using the --app option
# I called it app.py, so I will run with `flask --app app run` 
# It will run on http://127/0/0/1:5000 Ctrl+C to quit
# As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app. `flask run` should work, then 
# the server this launches is simple and good for testing but not for production/deployment


# import Flask
from flask import Flask

#add escape
from markupsafe import escape

# create an instance of Flask called app
# __name__ argument refers to applications module or package
# this argument tells Flask were to look for resources like templates and static files
app = Flask(__name__)

# use the route decorator to tell Flask which URL should trigger an associated function
@app.route('/')
# this function will return the message in the browser
def hello_world():
    return "<p>Hello, World!</p>"

# Bonus Info: If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:
# `$ flask run --host=0.0.0.0` to have operating system listen on all public IPs. 

# Enable debug mode with the --debug option
# So, `flask --app app --debug run` would show an interactive debugger in the browser
# Running this will give you a PIN. Console will display "debugger is active!" and the PIN

# You can use escape manually, as below
# <name> in the route captures a value from the URL and passes it to the view function.
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

# Using the route decorator, you can bind a function to a URL
# You can make parts of the URL dynamic and attach rules to a function as well
# You can add variable sections to a URL by marking sections with <variable_name>. 
# Your function then receives the <variable_name> as a keyword argument. 
# Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post you're referring to with an id that is an integer
    return f'Post{post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show what comes after path
    return f'Subpath {escape(subpath)}'

# There are two rules you should know about route names
# a route defined with a trailing slash is similar to a directory
# a route defined with no trailing slask is similar to a file. This helps keep URLs unique
# and avoids problems with search engines indexing the same page twice

@app.route('/projects/')
def projects():
    return 'The projects page'

@app.route('/about')
def about():
    return 'The about page'

# alternatively, you can use the reversing function for URL building
# the url_for() function accepts the name of a function for its first argument
# then any number of keyword arguments, corresponding to a part of the URL rule
# this approach can be more descriptive than hard coding. Can change them all programatically
# URL building handles escapes of special characters transparently


# Default HTTP method is "GET", but you can use the methods argument of the route() decorator 
# to handle different HTTP methods. Like the commented example below.

## from flask import request

## @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# alternativelly, you can seperate views for different methods into different functions. 
# as illustrated below. 

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()


# a simple example of how to render a template

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name=None):
    return render_template('example.html', name=name)
