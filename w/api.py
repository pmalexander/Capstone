from flask import render_template

from . import app
from .database import session

from flask import flash
from flask import SQLAlchemy
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
import os

import argparse
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#default page, shows up upon activation of the app if user is not already logged in
@app.route("/")
def start_page(page=1):
    return render_template("index.html")
    
@app.route("/login", methods=["GET"])
def login_g():
    return render_template("login.html")
    
#api requires separate function, borrowing from the function of what is provided on the side of html, remember json...
@app.route("/api/login", methods=["GET"])
def login_api_g():
    return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def login_p():
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Sorry, incorrect login information")
        return redirect(url_for("login_g"))

#ditto from the above regarding api display  
@app.route("/api/login", methods=["POST"])
def login_api_p():

#can be used as a template for the search process, remember to use the percentage sign to get portions of the text of locations, make sure to make it to the name of the location in the database    
#the search page, allows users to query park/nature reserve locations
@app.route("/search", methods=["GET"])
@login_required
def loc_search(name):
    connection = psycopg2.connect(database="w")
    cur = con.cursor(cursor_factory=e.DictCursor)
    cur.execute("select * from Locations where Name ILIKE '%s%'")
    l_rows = cur.fetchall()
 
    if l_rows is not None: 
        print(l_rows)
        l_rows = cur.fetchall()
    
    return render_template("search.html")

'''use this as locator when querying the the area based on location of latitude and longitudinal radius (also, replace the values)
l_query = "select id, name, region , ( 3959 * acos( cos( radians( %(latitude)s ) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians( %(longitude)s ) ) + sin( radians( %(latitude)s ) ) * sin( radians( lat ) ) ) ) AS distance FROM sightings HAVING distance < %(radius)s ORDER BY distance LIMIT %(limit)s" % {"latitude": lat, "longitude": lng, "radius": radius, "limit": lim}, visitors
'''
@app.route("/api/search", methods=["GET"])
@login_required
def loc_api_search(name):
    return location_names

#shows the locations by name of... location
@app.route("/search/<name>", methods=["GET"])
@login_required
def loc_search_parse_name(name):
    return render_template("search.html")

#shows the locations by name of... location
@app.route("/api/search/<name>", methods=["GET"])
@login_required
def loc_api_search_parse_name(name):
    return render_template("search.html")
    
#displays results of query from search page, ...
@app.route("/results")    
@login_required
def search_results():
    return render_template("results.html")
    
#displays results of query from search in api
@app.route("/api/results")
@login_required
def search_api_results():
    return render_template("results.html")
    
#displays information page comprising of general information, animals, plants, and natural features
@app.route("/information", methods=["GET"])
@login_required
def loc_information():
    return render_template("info.html")
    
#api display of information page
@app.route("/api/information", methods=["GET"])
@login_required
def loc_api_information():
    return render_template("info.html")

#directs users to checklist page to check off on items
@app.route("/checklist", methods=["GET"])
@login_required
def checklist_get():
    return render_template("checklist.html")    

#api format
@app.route("/api/checklist", methods=["GET"])
@login_required
def checklist_api_get():
    return render_template("checklist.html")    

@app.route("/checklist", methods=["POST"])
@login_required
def checklist_entries():
    return render_template("checklist.html")
    
@app.route("/api/checklist", methods=["POST"]
@login_required
def checklist_api_entries():
    return render_template("checklist.html")

#routes the user to the guide page (guide page is fixed, planned to be updated as time goes on to encompass multiple pages)
@app.route("/guide", methods=["GET"])
@login_required
def guide_get():
    return render_template("guide.html")   
    
@app.route("/api/guide", methods=["GET"])
@login_required
def guide_api_get():
    return render_template("guide.html")  

@app.route("/sighting", methods=["GET"])
@login_required
def sightings_g():
    return render_template("sighting.html")

#page for users to post sightings
@app.route("/api/sighting", methods=["GET"])
@login_required
def sighting_g():
    return render_template("sighting.html")
    
@app.route("/api/sighting", methods=["POST"])
@login_required
def sightings_p():
    return render_template("sighting.html")

#page for users to post sightings
@app.route("/api/sighting", methods=["POST"])
@login_required
def sighting_p():
    return render_template("sighting.html")    

#registration page for new users, user must register username using e-mail
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")

#api registration page
@app.route("/api/registration", methods=["GET", "POST"])
def registration_api():
    if request.method == "GET":
        return render_template("registration.html")

#provides logged user ability to logout
@app.route("/logout", methods=["GET"])
@login_required
def user_logout():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("start_page"))

#logs out user in api format    
@app.route("/api/logout", methods=["GET"])
@login_required
def user_logout_api():
    logout_user()
    flash"You have logged out.")
    return redirect(url_for("start_page"))

if __name__ == '__main__':
    