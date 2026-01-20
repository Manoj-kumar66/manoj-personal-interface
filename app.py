from flask import Flask, render_template, request, redirect, session, send_from_directory, abort
import os

app = Flask(__name__)
app.secret_key = "manoj_ultra_secret"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "my_files")

PIN = "6666"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("pin") == PIN:
            session["auth"] = True
            return redirect("/")
        else:
            return render_template("login.html", error="ACCESS DENIED")

    files = []
    if session.get("auth"):
        files = os.listdir(FILES_DIR)

    return render_template("login.html", files=files)


@app.route("/preview/<filename>")
def preview(filename):
    if not session.get("auth"):
        abort(403)

    path = os.path.join(FILES_DIR, filename)
    if not os.path.isfile(path):
        abort(404)

    if not filename.endswith(".txt"):
        return "Preview supported only for .txt files"

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


@app.route("/files/<filename>")
def download(filename):
    if not session.get("auth"):
        abort(403)
    return send_from_directory(FILES_DIR, filename, as_attachment=True)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
