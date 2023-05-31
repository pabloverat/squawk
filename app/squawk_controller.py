from bl.squawk_service import SquawkService
from flask import redirect, render_template, request, session

ss = SquawkService

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