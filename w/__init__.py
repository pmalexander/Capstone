import os

from flask import Flask

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "w.config.DevelopmentConfig")
app.config.from_object(config_path)

#imports user login
#imports views and filters to use in app
from . import views
from . import filters
from . import login