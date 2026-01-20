from flask import Flask, render_template, send_from_directory, request, session, redirect, abort
import os

app = Flask(__name__)
app.secret_key = "manoj_secret_key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "my_files")

PASSWORD = "6666"


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            session["auth"] = True
            return redirect("/")
        else:
            return render_template("login.html", error="ACCESS DENIED")

    files = []
    if session.get("auth"):
        files = os.listdir(FILES_DIR)

    return render_template("login.html", files=files)


@app.route("/files/<path:filename>")
def open_file(filename):
    if not session.get("auth"):
        abort(403)
    return send_from_directory(FILES_DIR, filename)


@app.route("/preview/<path:filename>")
def preview_file(filename):
    if not session.get("auth"):
        abort(403)

    file_path = os.path.join(FILES_DIR, filename)

    if not os.path.isfile(file_path):
        abort(404)

    if not filename.lower().endswith(".txt"):
        return "Preview supported only for .txt files"

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template, send_from_directory, request, session, redirect, abort
import os

app = Flask(__name__)
app.secret_key = "manoj_secret_key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "my_files")

PASSWORD = "6666"


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            session["auth"] = True
            return redirect("/")
        else:
            return render_template("login.html", error="ACCESS DENIED")

    files = []
    if session.get("auth"):
        files = os.listdir(FILES_DIR)

    return render_template("login.html", files=files)


@app.route("/files/<path:filename>")
def open_file(filename):
    if not session.get("auth"):
        abort(403)
    return send_from_directory(FILES_DIR, filename)


@app.route("/preview/<path:filename>")
def preview_file(filename):
    if not session.get("auth"):
        abort(403)

    file_path = os.path.join(FILES_DIR, filename)

    if not os.path.isfile(file_path):
        abort(404)

    if not filename.lower().endswith(".txt"):
        return "Preview supported only for .txt files"

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template, send_from_directory, request, session, redirect, abort
import os

app = Flask(__name__)
app.secret_key = "manoj_secret_key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "my_files")

PASSWORD = "6666"


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            session["auth"] = True
            return redirect("/")
        else:
            return render_template("login.html", error="ACCESS DENIED")

    files = []
    if session.get("auth"):
        files = os.listdir(FILES_DIR)

    return render_template("login.html", files=files)


@app.route("/files/<path:filename>")
def open_file(filename):
    if not session.get("auth"):
        abort(403)
    return send_from_directory(FILES_DIR, filename)


@app.route("/preview/<path:filename>")
def preview_file(filename):
    if not session.get("auth"):
        abort(403)

    file_path = os.path.join(FILES_DIR, filename)

    if not os.path.isfile(file_path):
        abort(404)

    if not filename.lower().endswith(".txt"):
        return "Preview supported only for .txt files"

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template, send_from_directory, request, session, redirect, abort
import os

app = Flask(__name__)
app.secret_key = "manoj_secret_key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "my_files")

PASSWORD = "6666"


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if request.form.get("password") == PASSWORD:
            session["auth"] = True
            return redirect("/")
        else:
            return render_template("login.html", error="ACCESS DENIED")

    files = []
    if session.get("auth"):
        files = os.listdir(FILES_DIR)

    return render_template("login.html", files=files)


@app.route("/files/<path:filename>")
def open_file(filename):
    if not session.get("auth"):
        abort(403)
    return send_from_directory(FILES_DIR, filename)


@app.route("/preview/<path:filename>")
def preview_file(filename):
    if not session.get("auth"):
        abort(403)

    file_path = os.path.join(FILES_DIR, filename)

    if not os.path.isfile(file_path):
        abort(404)

    if not filename.lower().endswith(".txt"):
        return "Preview supported only for .txt files"

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

