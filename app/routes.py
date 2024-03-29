from flask import Flask, render_template, url_for, flash, redirect
from app.models import User, Post 
from app.forms import RegistrationForm, LoginForm
<<<<<<< HEAD
from app import app, bcrypt, db
from flask_login import login_user, current_user, logout_user
=======
from app import app, db, bcrypt
>>>>>>> 821136f03ecba87f8c4d39361c6e9bf88f988d97
posts = [
          {
            'author': 'Md Shahid',
            'title' : 'Machine Learning',
            'content': 'This is Machine Learning',
            'date_posted': 'April 20, 2019'
          },
          {
            'author': 'Md Shahid',
            'title' : 'Deep Learning Learning',
            'content': 'This is Deep Learning',
            'date_posted': 'April 22, 2019'
          }
]

title = "ML/DL"

@app.route('/')
def hello():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title=title)


@app.route("/register", methods=['GET', 'POST'])
def register():
<<<<<<< HEAD
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
=======
	form = RegistrationForm()

	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') 
		user = User(username=form.username.data, email=form.email.data, password=hashed_password )
		db.session.add(user)
		db.session.commit()
		flash(f' Your account has been created for {form.username.data}!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)
>>>>>>> 821136f03ecba87f8c4d39361c6e9bf88f988d97

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
             login_user(user, remember=form.remember.data)
             return redirect(url_for('hello'))
        else:
             flash('Unsuccessful Sign in. Please Sign in again.', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('hello'))

