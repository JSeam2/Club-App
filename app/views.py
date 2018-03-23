from flask import render_template
from app import app
from app.forms import LoginForm, RegisterForm

@app.route('/', methods=['GET', 'POST'])
def index():
    #return app.send_static_file('index.html')
    login_form = LoginForm()
    reg_form = RegisterForm()

    #TODO
    if login_form.validate_on_submit():
        a = None # login view

    if reg_form.validate_on_submit():
        a = None # redirect to normal page and prompt user to login

    return render_template("index.html",
                           login_form = login_form,
                           reg_form = reg_form)


