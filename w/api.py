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
from flask_login import current_user

import requests
import json

#default page, shows up upon activation of the app if user is not already logged in
@app.route("/")
def start_page(page=1):
    return render_template("start.html")
    
@app.route("/login", methods=["GET"])
def login_g():
    return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def login_p():
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect login information")
        return redirect(url_for("login_g"))

#the search page, allows users to query park/nature reserve locations
@app.route("/search", methods=["POST"])
@login_required
def loc_search_post():
    search = Search_Query()
    return render_template("search.html")

#displays results of query from search page, ...
@app.route("/results")    
@login_required
def search_results():
    search_r = 
    return render_template("results.html")
    
@app.route("/information", methods=["GET"])
@login_required
def loc_information():
    return render_template("info.html")

@app.route("/checklist", methods=["GET"])
@login_required
def checklist_get():
    return render_template("checklist.html")    

@app.route("/checklist", methods=["POST"])
@login_required
def checklist_entries():
    return render_template("checklist.html")

#routes the user to the guide page (guide page is fixed, planned to be updated as time goes on to encompass multiple pages)
@app.route("/guide", methods=["GET"])
@login_required
def guide_get():
    return render_template("guide.html")   

#registration page for new users, user must register username using e-mail
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")

#provides logged user ability to logout
@app.route("/logout", methods=["GET]"])
@login_required
def user_logout():
    logout_user()
    flash("You have logged out.")
return redirect(url_for('search.html'))