from bl.squawk_service import SquawkService
from bl.thread_service import ThreadService
from bl.user_service import UserService
from flask import redirect, render_template, request, session

ss = SquawkService()
ts = ThreadService()
us = UserService()


def comment(is_reply_to):
  user_id = session['user_id']
  content = request.form['content']
  ss.create_squawk(content=content, is_reply_to=is_reply_to, user_id=user_id)
  return render_template("comment.html")

def new():
  user_id = session['user_id']
  content = request.form['content']
  ss.create_squawk(content, 0, user_id)
  return render_template("new.html")


def thread(squawk_id):
  user_id = session['user_id']

  squawk = ss.get_squawk(squawk_id=squawk_id)
  user = us.get_user(squawk.user_id).username
  squawk_info = (squawk, user)

  thread = ts.get_thread(squawk.squawk_id)
  thread_users = [us.get_user(squawk.user_id).username for squawk in thread]
  thread_info = list(zip(thread, thread_users))
  
  return render_template('thread.html', squawk_info=squawk_info, thread_info=thread_info, user_id=user_id)
