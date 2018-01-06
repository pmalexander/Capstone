#looks straight

from flask_login import LoginManager

from . import app
from .database import session, User

login_manager = LoginManager()
login_manager.init_app(app)