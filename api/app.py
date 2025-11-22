from flask import Flask, render_template, url_for
from api import utilities

app = Flask(__name__)

@app.route("/")
def index():
    projects = utilities.load_projects()
    return render_template('index.html.jinja', projects=projects)