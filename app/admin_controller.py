from flask import redirect, render_template, request, session


def admin():
    return render_template('admin.html')