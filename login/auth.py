from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from login.models import User


login = Blueprint('login', __name__, template_folder='templates')


@login.route("/", methods = ['POST','GET'])
def loginPage():
    if request.method == "POST":
        userName = request.form.get('userName')
        password = request.form.get('password')
        user = User.query.filter_by(userName = userName).first()
        if user:
            if user.password == password:
                return redirect(url_for('views.welcomePage'))
            else:
                flash('Incorrect Password', category='error')
        else:
            flash('User not found', category='error')
    return render_template('login.html')
