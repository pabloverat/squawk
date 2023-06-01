import admin_controller
import squawk_controller
import user_controller
from bl.event_service import EventService
from bl.user_service import UserService
from flask import Flask, redirect, render_template, request, session
from utils.database import Database

app = Flask(__name__)
app.secret_key = b'3fb893cec66673e6d7099fcf62356a634a72703f4f121b592ba64e0f5cff764e'

us = UserService()
ev = EventService()
app.add_url_rule('/home', view_func=user_controller.home, methods=["GET"])
app.add_url_rule('/user/<int:user_id>', view_func=user_controller.user, methods=["GET"])
app.add_url_rule('/new', view_func=squawk_controller.new, methods=["GET", "POST"])
app.add_url_rule('/comment/<int:is_reply_to>', view_func=squawk_controller.comment, methods=["GET", "POST"])
app.add_url_rule('/thread/<int:squawk_id>', view_func=squawk_controller.thread, methods=["GET", "POST"])
app.add_url_rule('/admin', view_func=admin_controller.admin, methods=["GET", "POST"])
app.add_url_rule('/dashboard', view_func=admin_controller.dashboard, methods=["GET", "POST"])

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    
    # trying to log in 
    login = us.login(username, password)
    # checking if user known
    if login == "user_unknown":
      return render_template('login.html', error='username unknown.')
    # checking if password correct
    if login == "password_mismatch":
      return render_template('login.html', error='incorrect password.')
    # password correct
    user = us.get_user_by_name(username)
    session['user_id'] = user.user_id
    ev.create_event(1, user.user_id)
    # login_user(user)
    # admin login
    if user.is_admin:
      return redirect('/admin')
    # user login
    return redirect('/home')
    
  return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
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



if __name__ == '__main__':
  app.run(use_reloader=True)