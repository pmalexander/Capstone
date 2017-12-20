from flask_login import LoginManager

from . import app
from . import session, User

login_manager = LoginManager()
login_manager.init_app(app)