import ui.admin_controller as admin_controller
import ui.main_controller as main_controller
import ui.squawk_controller as squawk_controller
import ui.user_controller as user_controller
from flask import Flask

app = Flask(__name__)
app.secret_key = b'3fb893cec66673e6d7099fcf62356a634a72703f4f121b592ba64e0f5cff764e'

# Main controller routes
app.add_url_rule('/', view_func=main_controller.index)
app.add_url_rule('/login', view_func=main_controller.login, methods=["GET", "POST"])
app.add_url_rule('/register', view_func=main_controller.signup, methods=["GET", "POST"])

# User controller routes
app.add_url_rule('/home', view_func=user_controller.home, methods=["GET"])
app.add_url_rule('/user/<int:user_id>', view_func=user_controller.user, methods=["GET"])

# Squawk controller routes
app.add_url_rule('/new', view_func=squawk_controller.new, methods=["GET", "POST"])
app.add_url_rule('/comment/<int:is_reply_to>', view_func=squawk_controller.comment, methods=["GET", "POST"])
app.add_url_rule('/thread/<int:squawk_id>', view_func=squawk_controller.thread, methods=["GET", "POST"])

# Admin controller routes
app.add_url_rule('/admin', view_func=admin_controller.admin, methods=["GET", "POST"])
app.add_url_rule('/dashboard', view_func=admin_controller.dashboard, methods=["GET", "POST"])

if __name__ == '__main__':
  app.run(use_reloader=True)