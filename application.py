from flask import Flask, render_template

#Create a new application as a Flask web application.
app = Flask(__name__)

#default webpage
@app.route("/")
def index():
    headline = "Formula1"
    return render_template("homepage.html", headline=headline)
@app.route("/drivers")
def drivers():
    headline = "Drivers"
    return render_template("drivers.html", headline=headline)

@app.route("/teams")
def teams():
    headline = "Teams"
    return render_template("teams.html", headline=headline)

@app.route("/standings")
def standings():
    headline = "Standings"
    return render_template("standings.html", headline=headline)

@app.route("/calendar")
def races():
    headline = "Calendar"
    return render_template("calendar.html", headline=headline)
