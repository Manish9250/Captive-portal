from flask import render_template, url_for, redirect, request
from flask import current_app as app

# Home page
@app.route("/")
def home_page():
    return render_template("index.html")