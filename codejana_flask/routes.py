#from bcrypt import methods
from codejana_flask import app, db
from sre_constants import SUCCESS
from flask import Flask, render_template,redirect,url_for,flash
from codejana_flask.forms import RegistrationForm, LoginForm
from codejana_flask.models import User 
 

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Home')



@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/games')
def games():
    return render_template('games.html', title='Games')

@app.route('/about/user')
def user():
    return render_template('user.html', title='User')

@app.route('/register',methods=['POST','GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Cuenta creada satisfactoriamente {form.username.data}', category = 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register',form=form)





@app.route('/login', methods=['POST', 'GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if form.email.data==user.email and form.password.data==user.password:
            flash(f'Login successful for {form.email.data}', category='success')

            return redirect(url_for('user'))
        else:
            flash(f'Login unsuccessful for {form.email.data}', category='danger')
    return render_template('login.html', title='Login', form=form)