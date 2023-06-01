from bl.event_service import EventService
from bl.squawk_service import SquawkService
from bl.thread_service import ThreadService
from bl.user_service import UserService
from flask import redirect, render_template, request, session, url_for

ev = EventService()
ss = SquawkService()
ts = ThreadService()
us = UserService()

def comment(is_reply_to):
  user_id = session['user_id']
  
  if request.method == 'POST':
    content = request.form['content']
    ss.create_squawk(content=content, is_reply_to=is_reply_to, user_id=user_id)
    ev.create_event(3, user_id)
    return redirect(url_for('thread', squawk_id=is_reply_to))
  return render_template("comment.html", user_id=user_id, is_reply_to=is_reply_to)

def new():
  user_id = session['user_id']  
  if request.method == 'POST':
    content = request.form['content']
    ss.create_squawk(content, 0, user_id)
    ev.create_event(2, user_id)
    return redirect('/home')
    
  return render_template("new.html", user_id=user_id)

def thread(squawk_id):
  user_id = session['user_id']

  squawk = ss.get_squawk(squawk_id=squawk_id)
  user = us.get_user(squawk.user_id).username
  squawk_info = (squawk, user)

  thread = ts.get_thread(squawk.squawk_id)
  thread_users = [us.get_user(squawk.user_id).username for squawk in thread]
  thread_info = list(zip(thread, thread_users))
  
  return render_template('thread.html', squawk_info=squawk_info, thread_info=thread_info, user_id=user_id)
