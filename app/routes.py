#Returns rendered pages from view function
#Author: Edit:

from flask import render_template
#This function takes a template filename and a variable list of template arguments and returns the same template
#But with all the placeholders in it replaced with actual values.
from app import app

#The "@app.route()" below are decorators(Python feature), a decorator modifies the function that follows it.
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    #posts is a list of dictionaries, where 'author' is also a dictionary
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
