from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

FILES_DIR = "my_files"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "Manoj" and request.form["password"] == "6666":
            return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if not os.path.exists(FILES_DIR):
        files = []
    else:
        files = os.listdir(FILES_DIR)
    return render_template("dashboard.html", files=files)


@app.route("/preview/<filename>")
def preview_file(filename):
    return send_from_directory(FILES_DIR, filename)


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(FILES_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    app.run()
