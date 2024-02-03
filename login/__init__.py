from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    root = Flask(__name__)
    root.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/users.db"
    root.config["SECRET_KEY"] = "GitHub"
    db.init_app(root)

    from login.auth import login
    from login.views import views
    root.register_blueprint(views)
    root.register_blueprint(login)

    from login.models import User
    with root.app_context():
        db.create_all()

    from flask_login import LoginManager
    login_manager = LoginManager()    
    login_manager.init_app(root)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)


    return root