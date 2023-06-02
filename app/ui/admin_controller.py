from bl.event_service import EventService
from bl.squawk_service import SquawkService
from bl.user_service import UserService
from flask import redirect, render_template, request, session

es = EventService()
ss = SquawkService()
us = UserService()


def admin():
  return render_template('admin.html')

def dashboard():
  popular_squawk_tuple, active_user_tuple, todays_logins_count = es.get_report()
  active_user = us.get_user(user_id=active_user_tuple[0]) if active_user_tuple else None
  events_amount = active_user_tuple[1] if active_user_tuple else 0
  popular_squawk = ss.get_squawk(squawk_id=popular_squawk_tuple[0]) if popular_squawk_tuple else None
  replies_amount = popular_squawk_tuple[1] if popular_squawk_tuple else 0
  return render_template('dashboard.html', active_user=active_user, popular_squawk=popular_squawk, todays_logins=todays_logins_count[0], events_amount=events_amount, replies_amount=replies_amount)