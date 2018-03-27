'''comment'''

import json
import csv
import os

from . import app
from w.database import session, Location, Fauna, Flora, Feature, Base

from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask import flash
from flask import request, redirect, url_for, render_template, jsonify, request

from w.database import User, Sighting #added w to .database o 3/21/2018, might reconsider changing back to .

from werkzeug.security import check_password_hash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import login_manager
from flask_login import current_user

#pulls the names from the location, fauna, flora, and feature tables, attributes location, fauna, etc. from dictionary to the class
name = request.args.get('searchq', ' ')
categories = {'Location':Location, 'Fauna':Fauna, 'Flora':Flora, 'Feature':Feature}

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
        return redirect(url_for('search_all'))
     
#login page for users, bypass if user is previously logged in
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
@app.route("/authorized/user/content/search", methods=["GET"])
@app.route("/authorized/user/content/search/?searchq=none", methods=["GET"])
#@login_required
def search_all():
    gen_query = "%%"
    entries = session.query(Location).all()
    return render_template("search.html", entries=entries)

@app.route("/authorized/user/content/search/all/", methods=["GET"])
@app.route("/authorized/user/content/search/all/?searchq=none", methods=["GET"])
@login_required
#def search_by_name(name):
#    gen_query = "'%" + name + "%'"
#    entries = session.query()
#    return render_template("search.html", entries=entries)

@app.route("/authorized/user/content/search/location/", methods=["GET"])
@app.route("/authorized/user/content/search/location/?searchq=none", methods=["GET"])
@login_required
def search_by_location():
    print(name)
    loc_query = "'%" + name + "%'"
    entries = session.filter(Location.name.like(loc_query))
#    lopt = session.query(Option).filter_by(question=qinst)
#    entries = session.query(Location).filter(Location.name.like)
    return render_template("search.html", entries=entries)

@app.route("/authorized/user/content/search/fauna/", methods=["GET"])
@app.route("/authorized/user/content/search/fauna/?searchq=none", methods=["GET"])
@login_required
def search_by_fauna():
    print(name)
    fauna_query = "'%" + name + "%'"
    entries = session.filter(Fauna.name.like(fauna_query))
    return render_template("search.html", entries=entries)

@app.route("/authorized/user/content/search/flora/", methods=["GET"])
@app.route("/authorized/user/content/search/flora/?searchq=none", methods=["GET"])
#@login_required
def search_by_flora():
    print(name)
    flora_query = "'%" + name + "%'"
    entries = session.filter(Flora.name.like(flora_query))
    return render_template("search.html", entries=entries)
    
@app.route("/authorized/user/content/search/feature/", methods=["GET"])
@app.route("/authorized/user/content/search/feature/?searchq=none", methods=["GET"])
#@login_required
def search_by_feature():
    feature_query = "'%" + name + "%'"
    entries = session.filter(Feature.name.like(feature_query))
    return render_template("search.html", entries=entries)

#displays information page comprising of general information, animals, plants, and natural features
@app.route("/authorized/user/content/information", methods=["GET"])
@login_required
def loc_information():
    return render_template("information.html")
    
#directs users to checklist page to check off on items
@app.route("/authorized/user/content/checklist", methods=["GET"])
#@login_required
def checklist_get():
    return render_template("checklist.html")    

@app.route("/authorized/user/content/checklist", methods=["POST"])
#@login_required
def checklist_entry():
    return render_template("checklist.html")
    
#routes the user to the guide page (guide page is fixed, planned to be updated as time goes on to encompass multiple pages)
@app.route("/authorized/user/content/guide", methods=["GET"])
#@login_required
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
        author=current_user["author"]
    )
    session.add(sighting)
    session.commit()
    return render_template("sighting.html")

#provides logged user ability to logout
@app.route("/logout", methods=["GET"])
#@login_required
def user_logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("login_g"))
