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
    
@app.route("/login", methods=["GET"])
def login_g():
    return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def login_p():
    email = request.form["email"]
    password = request.form["password"]
    user = session.query(User).filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Sorry, incorrect login information")
        return redirect(url_for("login_g"))

#can be used as a template for the search process, remember to use the percentage sign to get portions of the text of locations, make sure to make it to the name of the location in the database    
#the search page, allows users to query park/nature reserve locations
@app.route("/search", methods=["GET", "POST"])
@login_required
def loc_search(name,):
    connection = psycopg2.connect(database="wild")
    cur = con.cursor(cursor_factory=e.DictCursor)
    cur.execute("select * from Locations where Name like '%%'", (name,))
    l_rows = cur.fetchall()

    if l_rows is not None: 
        print(l_rows)
        l_rows = cur.fetchall()
    
    return render_template("search.html")

'''use this as locator when querying the the area based on location of latitude and longitudinal radius (also, replace the values)
l_query = "select id, name, region , ( 3959 * acos( cos( radians( %(latitude)s ) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians( %(longitude)s ) ) + sin( radians( %(latitude)s ) ) * sin( radians( lat ) ) ) ) AS distance FROM sightings HAVING distance < %(radius)s ORDER BY distance LIMIT %(limit)s" % {"latitude": lat, "longitude": lng, "radius": radius, "limit": lim}, visitors
'''

#shows the locations by name of... location
@app.route("/search/<name>", methods=["GET", "POST"])
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
    return render_template("search.html")

    """Retrieve the snippet with a given name. If there is no such snippet, return '404: Snippet Not Found'. Returns the snippet."""
    #taken from snippets, review this to see how I can parse info from there
    #def get(name,):
    #logging.info("Retrieving snippet {!r}".format(name,))
    #with connection, connection.cursor() as cursor:
    #    cursor.execute("select message from snippets where keyword=%s", (name,))
    #    fetch_row = cursor.fetchone()
    #if not fetch_row: 
    #    # No snippet was found with that name.
    #    return "404: Snippet Not Found"
    #return fetch_row[0]
    #taken from snippets

@app.route("/results", methods=["GET"])
@login_required
def search_results(location):
    l_results = User.

#displays information page comprising of general information, animals, plants, and natural features
@app.route("/information", methods=["GET"])
@login_required
def loc_information():
    
    return render_template("info.html")
    
#directs users to checklist page to check off on items
@app.route("/checklist", methods=["GET"])
@login_required
def checklist_get():
    return render_template("checklist.html")    

@app.route("/checklist", methods=["POST"])
@login_required
def checklist_entry():
    return render_template("checklist.html")
    
#routes the user to the guide page (guide page is fixed, planned to be updated as time goes on to encompass multiple pages)
@app.route("/guide", methods=["GET"])
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

@app.route("/sighting", methods=["GET"])
@login_required
def sightings_g():
    return render_template("sighting.html")

#registration page for new users, user must register username using e-mail
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")

#provides logged user ability to logout
@app.route("/logout", methods=["GET"])
@login_required
def user_logout():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("start_page"))

if __name__ == '__main__':
    