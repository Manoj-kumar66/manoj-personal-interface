from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

FILES_DIR = "my_files"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # simple demo login
        if username == "admin" and password == "admin":
            return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    files = []
    if os.path.exists(FILES_DIR):
        files = os.listdir(FILES_DIR)
    return render_template("dashboard.html", files=files)


@app.route("/files/<filename>")
def open_file(filename):
    return app.send_static_file(f"../{FILES_DIR}/{filename}")


# ✅ REQUIRED FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
