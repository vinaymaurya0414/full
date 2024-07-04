from flask import Flask
from flask_login import LoginManager
from .models import User

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Simulate user lookup
        return User(user_id, "username", "password")


    from . import routes
    app.register_blueprint(routes.bp)

    return app
