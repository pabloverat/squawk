from bl.event_service import EventService
from bl.user_auth import DBAuthStrategy
from bl.user_service import UserService
from flask import redirect, render_template, request, session

us = UserService()
ev = EventService()
auth_strategy = DBAuthStrategy()


def index():
  return render_template('index.html')


def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    
    if auth_strategy.authenticate(username, password):
      user = us.get_user_by_name(username)
      session['user_id'] = user.user_id
      ev.create_event(1, user.user_id)
      if user.is_admin:
        return redirect('/admin')
      return redirect('/home')
    else:
      return render_template('login.html', error='Incorrect username or password.')
    
  return render_template('login.html')


def signup():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    confirmPassword = request.form['confirmPassword']
    if password != confirmPassword:
      return render_template('register.html', error='Passwords do not match.')
    if us.signup(username, password):
      return redirect('/')
    else:
      return render_template('register.html', error='Username already exists.')    
  
  return render_template('register.html')