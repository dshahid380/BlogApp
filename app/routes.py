from flask import Flask, render_template, url_for, flash, redirect
from app.models import User, Post 
from app.forms import RegistrationForm, LoginForm
from app import app
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
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('hello'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'dshahid3805@gmail.com' and form.password.data == 'a':
			flash('Successfully logged in', 'success')
			return redirect(url_for('hello'))
		else:
			flash('Unsuccessful Sign in. Please Sign in again.', 'danger')

	return render_template('login.html', title='Login', form=form)