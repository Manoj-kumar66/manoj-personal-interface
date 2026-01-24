from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "my_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# demo credentials
USERNAME = "Manoj"
PASSWORD_HASH = generate_password_hash("6666")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (
            request.form["username"] == USERNAME
            and check_password_hash(PASSWORD_HASH, request.form["password"])
        ):
            session["user"] = USERNAME
            return redirect(url_for("dashboard"))
        return "Invalid login"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    files = []
    for root, dirs, filenames in os.walk(UPLOAD_FOLDER):
        for name in filenames:
            full_path = os.path.join(root, name)
            files.append(full_path.replace(UPLOAD_FOLDER + "/", ""))

    return render_template("dashboard.html", files=files)


@app.route("/upload", methods=["POST"])
def upload():
    if "user" not in session:
        return redirect(url_for("login"))

    uploaded_files = request.files.getlist("files")

    for file in uploaded_files:
        if file.filename == "":
            continue

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        file.save(filepath)

    return redirect(url_for("dashboard"))


@app.route("/download/<path:filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
