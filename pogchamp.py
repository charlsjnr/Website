import sqlite3
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

@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT pogfaces, classification, type, date FROM pogchamps JOIN gender ON pogchamps.gender_id = gender.id JOIN type_of_face ON pogchamps.facetype_id = type_of_face.id"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)