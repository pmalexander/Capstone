import os

from flask import Flask

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "w.config.Config")
app.config.from_object(config_path)

#imports user login
#imports filters to use in app
#app dummied out, seems to be causing conflicts
from . import api
from . import app
from . import filters
from . import login


