from flask import Flask, render_template, send_from_directory, request, redirect, url_for, session, abort
import os

app = Flask(__name__)
app.secret_key = "manoj_secret_key_change_later"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "my_files")

PASSWORD = "6666"   # 🔐 change this anytime

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            session["auth"] = True
            return redirect("/panel")
        return render_template("login.html", error="ACCESS DENIED")
    return render_template("login.html")

@app.route("/panel")
def panel():
    if not session.get("auth"):
        return redirect("/")
    files = os.listdir(FILES_DIR)
    return render_template("index.html", files=files)

@app.route("/files/<path:filename>")
def open_file(filename):
    if not session.get("auth"):
        abort(403)
    return send_from_directory(FILES_DIR, filename)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
