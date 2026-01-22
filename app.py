from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # simple demo login
        if username == "manoj" and password == "6666":
            return redirect(url_for("dashboard"))
        else:
            return render_template("index.html", error="Invalid credentials")

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
