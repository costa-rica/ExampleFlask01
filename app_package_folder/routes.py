from flask import Blueprint
from flask import render_template, request, abort, render_template_string

users = Blueprint('users', __name__)

@users.route("/")
def home():
    return "Home Page"

@users.route('/messages/<idx>')
def message(idx):
    idx=int(idx)
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        return render_template_string("<h1> Messages: {{ messages }}</h1>", messages=messages[idx])
    except IndexError:
        abort(500)