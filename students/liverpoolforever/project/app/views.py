from flask import render_template,flash,redirect,request
from app import app
from .forms import InputForm,LoginForm

@app.route('/')
def simple_index():
    return "Hello World Flask Webservice"

@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/dashboard')
def dashboard():
    form = InputForm()
    return render_template('input.html',title='Liverpool Rocks',form=form)

#Accept input from dashboard
@app.route('/acceptInput' , methods=['GET','POST'])
def accept_input():
    field1 = request.form['field1']
    field2 = request.form['field2']
    res = "The response is {} and {} ".format(field1,field2)
    return res

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

