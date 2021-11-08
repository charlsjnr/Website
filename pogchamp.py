import sqlite3
import time
from flask import Flask, g, render_template, request, redirect

app = Flask(__name__)
#this connects the code to the correct database for the website
DATABASE = "Database.db"

def get_db():
    db = getattr (g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

#renders home page
@app.route("/")
def home():
    return render_template("home.html")

#renders database page, ordering from oldest pogchamp
@app.route("/pogfaces")
def contents(): 
    cursor = get_db().cursor()
    sql = "SELECT pogfaces, classification, type, date, filename FROM pogchamps JOIN gender ON pogchamps.gender_id = gender.id JOIN type_of_face ON pogchamps.facetype_id = type_of_face.id"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

#orders database from most recent pogchamp
@app.route("/pogfaces_recent")
def pogfaces_recent():
    cursor = get_db().cursor()
    sql = "SELECT pogfaces, classification, type, date, filename FROM pogchamps JOIN gender ON pogchamps.gender_id = gender.id JOIN type_of_face ON pogchamps.facetype_id = type_of_face.id ORDER BY date DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

#orders database in alphabetical order
@app.route("/pogfaces_namea")
def pogfaces_namea():
    cursor = get_db().cursor()
    sql = "SELECT pogfaces, classification, type, date, filename FROM pogchamps JOIN gender ON pogchamps.gender_id = gender.id JOIN type_of_face ON pogchamps.facetype_id = type_of_face.id ORDER BY pogfaces"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

#orders database in reverse alphabetical order
@app.route("/pogfaces_namez")
def pogfaces_namez():
    cursor = get_db().cursor()
    sql = "SELECT pogfaces, classification, type, date, filename FROM pogchamps JOIN gender ON pogchamps.gender_id = gender.id JOIN type_of_face ON pogchamps.facetype_id = type_of_face.id ORDER BY pogfaces DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

#filters database to show only male faces
@app.route("/pogfaces_men")
def pogfaces_men():
    cursor = get_db().cursor()
    sql = "SELECT pogfaces, classification, type, date, filename FROM pogchamps JOIN gender ON pogchamps.gender_id = gender.id JOIN type_of_face ON pogchamps.facetype_id = type_of_face.id WHERE gender.id = '1'"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

#filters database to show only female faces
@app.route("/pogfaces_women")
def pogfaces_women():
    cursor = get_db().cursor()
    sql = "SELECT pogfaces, classification, type, date, filename FROM pogchamps JOIN gender ON pogchamps.gender_id = gender.id JOIN type_of_face ON pogchamps.facetype_id = type_of_face.id WHERE gender.id = '2'"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

#filters database to show only non-binary pogchamps
@app.route("/pogfaces_non-binary")
def pogfaces_nonbinary():
    cursor = get_db().cursor()
    sql = "SELECT pogfaces, classification, type, date, filename FROM pogchamps JOIN gender ON pogchamps.gender_id = gender.id JOIN type_of_face ON pogchamps.facetype_id = type_of_face.id WHERE gender.id = '3'"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)