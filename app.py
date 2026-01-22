from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import os

app = Flask(__name__)
app.secret_key = "manoj_secret_key"

FILES_DIR = "my_files"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "manoj" and password == "6666":
            return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    files = os.listdir(FILES_DIR)
    return render_template("dashboard.html", files=files)


@app.route("/files/<filename>")
def open_file(filename):
    return send_from_directory(FILES_DIR, filename, as_attachment=False)


@app.route("/logout")
def logout():
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
