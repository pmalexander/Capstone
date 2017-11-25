from flask import render_template

from . import app
from w.database import session

from flask import flash
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import login_manager
from werkzeug.security import check_password_hash
from flask import request, redirect, url_for

@app.route("/search", methods=["GET"])
def loc_search():
    return render_template("search.html")
    

@app.route("/checklist", methods=["GET"])
def checklist_get():
    return render_template("checklist.html")    
    
@app.route("/guide", methods=["GET"])
def guide_get():
    return render_template("guide.html")   