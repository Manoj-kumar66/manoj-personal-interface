from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "manoj" and password == "6666":
            return redirect(url_for("dashboard"))
        else:
            return render_template("index.html", error="Invalid credentials")

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
