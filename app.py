from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "manoj_secret_key"

# ---------------- CONFIG ----------------
UPLOAD_FOLDER = "my_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ---------------- LOGIN CREDENTIALS ----------------
USERNAME = "Manoj"
PASSWORD_HASH = generate_password_hash("6666")  # password = 1234

# ---------------- ROUTES ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and check_password_hash(PASSWORD_HASH, password):
            session["user"] = username
            return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    files = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template("dashboard.html", files=files)


@app.route("/upload", methods=["POST"])
def upload():
    if "user" not in session:
        return redirect(url_for("login"))

    if "file" not in request.files:
        return redirect(url_for("dashboard"))

    file = request.files["file"]

    if file.filename == "":
        return redirect(url_for("dashboard"))

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    return redirect(url_for("dashboard"))


@app.route("/download/<filename>")
def download(filename):
    if "user" not in session:
        return redirect(url_for("login"))

    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

