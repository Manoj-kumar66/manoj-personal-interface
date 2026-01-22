from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

FILES_FOLDER = "my_files"

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
    files = []
    if os.path.exists(FILES_FOLDER):
        files = os.listdir(FILES_FOLDER)

    return render_template("dashboard.html", files=files)


@app.route("/files/<filename>")
def open_file(filename):
    return open(os.path.join(FILES_FOLDER, filename)).read()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
