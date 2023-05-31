from bl.squawk_service import SquawkService
from bl.thread_service import ThreadService
from bl.user_service import UserService
from flask import Flask, redirect, render_template, request, session

us = UserService()
ss = SquawkService()
ts = ThreadService()

def home():
  user_id = session['user_id']
  squawks = []
  last20 = ss.get_last(20,-1)
  for i in last20:
    thread = ts.get_thread(i.squawk_id)
    thread_users = [us.get_user(squawk.user_id).username for squawk in thread]
    thread_info = list(zip(thread, thread_users))
    user = us.get_user(i.user_id).username
    squawks.append((i, user, thread_info))
  return render_template('home.html', squawks=squawks, user_id=user_id)

def user(user_id):
  squawks = []
  username = us.get_user(user_id).username
  last10 = ss.get_last(10,user_id)
  for i in last10:
    thread = ts.get_thread(i.squawk_id)
    thread_users = [us.get_user(squawk.user_id).username for squawk in thread]
    thread_info = list(zip(thread, thread_users))
    user = us.get_user(i.user_id).username
    squawks.append((i, user, thread_info))
  return render_template('user.html', username=username, squawks=squawks)