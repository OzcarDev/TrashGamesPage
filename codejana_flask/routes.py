
from codejana_flask import app, db, bcrypt
from sre_constants import SUCCESS
from flask import Flask, render_template,redirect,url_for,flash
from codejana_flask.forms import RegistrationForm, LoginForm
from codejana_flask.models import User 
from flask_login import login_user, logout_user, current_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('user'))
    form=RegistrationForm()
    if form.validate_on_submit():
        encrypted_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Cuenta creada satisfactoriamente {form.username.data}', category = 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register',form=form)





@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash(f'Login successful for {form.email.data}', category='success')

            return redirect(url_for('user'))
        else:
            flash(f'Login unsuccessful for {form.email.data}', category='danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))