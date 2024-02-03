from flask import Blueprint, render_template

views = Blueprint('views', __name__, template_folder='templates')

@views.route("/welcome", methods = ["GET"])
def welcomePage():
    return render_template('logged.html')