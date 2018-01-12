import json
import csv
import os

from . import app
from .database import session

from flask import flash
from flask import SQLAlchemy
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import login_manager
from flask_login import current_user
from werkzeug.security import check_password_hash
from flask import request, redirect, url_for, render_template, jsonify, request

from .database import User

#sets default display of results to 10 per page
PAGINATE_BY = 10

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
    if current_user.is_authenticated:
        return redirect(url_for('search'))
    return render_template("index.html")
    
#registration page for new users, user must register username using e-mail, registration allows ability to personalize app (save pictures, plans, checklists, etc.), if logged in, bypass this stage
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")
    elif request.method == "POST":
        pass

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
    pass

#user page with personal effects?
@app.route("/authorized/user/<username>")
@login_required
def user_personal(username):
    pass

#NEED TO USE SESSION QUERY FOR THE SEARCH FUNCTION 12/19/2017, IF THERE IS A CHANGE HERE, I'D HAVE TO HEAD STRAIGHT TO THE REFERENCED ITEM
#can be used as a template for the search process, remember to use the percentage sign to get portions of the text of locations, make sure to make it to the name of the location in the database    
#the search page, allows users to query park/nature reserve locations
@app.route("/authorized/user/search", methods=["GET", "POST"])
@login_required
def loc_search(name,):
    connection = psycopg2.connect(database="wild")
    cur = con.cursor(cursor_factory=e.DictCursor)
    cur.execute("select * from Locations where Name like '%%'", (name,))
    l_rows = cur.fetchall()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect((url_for('results', query=form.search.data)))
        if not l_rows:
            return "Cannot locate entry"
    return render_template("search.html")

'''use this as locator when querying the the area based on location of latitude and longitudinal radius (also, replace the values)
l_query = "select id, name, region , ( 3959 * acos( cos( radians( %(latitude)s ) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians( %(longitude)s ) ) + sin( radians( %(latitude)s ) ) * sin( radians( lat ) ) ) ) AS distance FROM sightings HAVING distance < %(radius)s ORDER BY distance LIMIT %(limit)s" % {"latitude": lat, "longitude": lng, "radius": radius, "limit": lim}, visitors
'''

#shows the locations by name of... location, returns error if there are no matches to the query
@app.route("/authorized/user/search/<name>", methods=["GET", "POST"])
@login_required
def loc_search_parse_name(name,):
    connection = psycopg2.connect(database="wild")
    cur = con.cursor(cursor_factory=e.DictCursor)
    cur.execute("select * from Locations where Name like '%%'", (name,))
    l_rows_parse_name = cur.fetchone()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect((url_for('results', query=form.search.data)))
    if not l_rows_parse_name:
        return "Cannot locate entry."
    #has to return the resultl
    return render_template("search.html")

#displays information page comprising of general information, animals, plants, and natural features
@app.route("/authorized/user/content/information", methods=["GET"])
@login_required
def loc_information():
    l_information = User. 
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
    start = page_index * PAGINATE_BY
    end = start + PAGINATE_BY

    total_pages = (count - 1) // PAGINATE_BY + 1
    has_next = page_index < total_pages - 1
    has_prev = page_index > 0
    return render_template("guide.html")   
    
@app.route("guide/?limit=10")
@app.route("guide/page/2?limit=10")

@app.route("/authorized/user/content/sighting", methods=["GET"])
@login_required
def sightings_g():
    return render_template("sighting.html")

#provides logged user ability to logout
@app.route("/logout", methods=["GET"])
@login_required
def user_logout():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("start_page"))

if __name__ == '__main__':
    