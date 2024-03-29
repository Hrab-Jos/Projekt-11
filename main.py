from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
import json

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def to_pretty_notifications_json(notifications):

    return json.dumps(notifications, default=lambda x: {'id': x.id, 'header': x.header, 'datetime': x.time.strftime('%d.%m.%Y %H:%M')})


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@db:5432/postgres'
    app.static_folder = 'static'
    app.static_url_path = '/static'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    import json

    app.jinja_env.filters['to_pretty_notifications_json'] = to_pretty_notifications_json

    return app


app = create_app()