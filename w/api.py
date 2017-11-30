from flask import render_template

from . import app
from .database import session

from flask import flash
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import login_manager
from werkzeug.security import check_password_hash
from flask import request, redirect, url_for

from .database import User

#sets the default page for the app, the search page complete with search bar
@app.route("/")
@login_required
def search_start(page=1):
    return render_template("search.html")
    
@app.route("/search", methods=["GET"])
@login_required
def loc_search_g():
    return render_template("search.html")
    
@app.route("/search", methods=["POST"])
@login_required
def loc_search_p():
    return render_template("search.html")

@app.route("/information", methods=["GET"])
@login_required
def loc_information():
    return render_template("info.html")

@app.route("/checklist", methods=["GET"])
@login_required
def checklist_get():
    return render_template("checklist.html")    

@app.route("/checklist", methods=["POST"])
def checklist_entries():
    return
    
@app.route("/guide", methods=["GET"])
def guide_get():
    return render_template("guide.html")   

#provides logged user ability to logout
@app.route("/logout", methods=["GET]"])
@login_required
def user_logout():
    logout_user()
    flash("You have logged out.")
return redirect(url_for('search.html'))