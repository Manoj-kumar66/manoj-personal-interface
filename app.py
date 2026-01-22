from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "manoj_secret_key"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "manoj" and password == "6666":
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="ACCESS DENIED")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
