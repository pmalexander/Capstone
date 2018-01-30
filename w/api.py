'''comment'''

import json
import csv
import os

from . import app
from w.database import session, Location, Base

from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask import flash
from flask import request, redirect, url_for, render_template, jsonify, request

from .database import User, Sighting

from werkzeug.security import check_password_hash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import login_manager
from flask_login import current_user

#default page, shows up upon activation of the app if user is not already logged in
@app.route("/")
@login_required
def start_page(page=1):
    return redirect(url_for('search'))

#registration page for new users, user must register username using e-mail, registration allows ability to personalize app (save pictures, plans, checklists, etc.), if logged in, bypass this stage
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")
    elif request.method == "POST":
        return render_template("search.html")
     
#login page for users, bypass if user is previously logged  in
@app.route("/login", methods=["GET", "POST"])
def login_g():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Sorry, incorrect login information")
        return redirect(url_for("login_g"))  
    login_user(user)
    return redirect(url_for('search')) 

#user page with personal effects?
#@app.route("/authorized/user/<username>")
#@login_required
#def user_personal(username):
#    pass

#NEED TO USE SESSION QUERY FOR THE SEARCH FUNCTION 12/19/2017, IF THERE IS A CHANGE HERE, I'D HAVE TO HEAD STRAIGHT TO THE REFERENCED ITEM
#can be used as a template for the search process, remember to use the percentage sign to get portions of the text of locations, make sure to make it to the name of the location in the database    
#the search page, allows users to query park/nature reserve locations
@app.route("/authorized/user/content/search", methods=["GET", "POST"])
@login_required
def loc_search(name,):
    location_search = session.query(Location).filter(Location.name.like('%%')).all()
    if request.method == "POST":
        return redirect(url_for('search', location_search=location_search))
    pass

@app.route("/authorized/user/content/search/<query>", methods=["GET", "POST"])
@login_required
def loc_query(name,):
    location_search = session.query(Location).filter(Location.name.like('%%')).all()
    return redirect(url_for('search', location_search=location_search))

#displays information page comprising of general information, animals, plants, and natural features
@app.route("/authorized/user/content/information", methods=["GET"])
@login_required
def loc_information():
    return render_template("information.html")
    
@app.route("/authorized/user/content/information/<location_id>", methods=["GET"])
@login_required
def loc_information_id():
#    l_information_id = User.
    return render_template("information.html")
    
#directs users to checklist page to check off on items
@app.route("/authorized/user/content/checklist", methods=["GET"])
@login_required
def checklist_get():
    return render_template("checklist.html")    

@app.route("/authorized/user/content/checklist", methods=["POST"])
@login_required
def checklist_entry():
    return render_template("checklist.html")
    
#routes the user to the guide page (guide page is fixed, planned to be updated as time goes on to encompass multiple pages)
@app.route("/authorized/user/content/guide", methods=["GET"])
@login_required
def guide_get():
    return render_template("guide.html")   

#provides users with means to post sightings to share with others, presence of animals and/or plants in certain locations to update others, etc.    
@app.route("/authorized/user/content/sighting", methods=["GET"])
@login_required
def sightings_g():
    return render_template("sighting.html")

@app.route("/authorized/user/content/sighting", methods=["GET"])
@login_required
def sightings_p():
    sighting = Sighting(
        title=request.form["title"],
        content=request.form["content"],
    )
    session.add(sighting)
    session.commit()
    return render_template("sighting.html")

#provides logged user ability to logout
@app.route("/logout", methods=["GET"])
@login_required
def user_logout():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("index"))
