from flask import Flask
from config import config
from .models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

login_manager.login_view = 'loginPage'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


from . import routes
from . import models