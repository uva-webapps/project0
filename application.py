from flask import Flask, render_template

#Create a new application as a Flask web application.
#Not used for this project
app = Flask(__name__)

#default webpage
@app.route("/")
def index():
    #gives the headline for the webpage
    headline = "Formula1"
    return render_template("homepage.html", headline=headline)
#webpage that shows the F1 drivers
@app.route("/drivers")
def drivers():
    #gives the headline for the webpage
    headline = "Drivers"
    return render_template("drivers.html", headline=headline)
#webpage that shows the F1 teams
@app.route("/teams")
def teams():
    #gives the headline for the webpage
    headline = "Teams"
    return render_template("teams.html", headline=headline)
#webpage that shows the F1 Standings
@app.route("/standings")
def standings():
    #gives the headline for the webpage
    headline = "Standings"
    return render_template("standings.html", headline=headline)
#webpage that shows the F1 race calendar
@app.route("/calendar")
def races():
    #gives the headline for the webpage
    headline = "Calendar"
    return render_template("calendar.html", headline=headline)
