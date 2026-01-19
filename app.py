from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "my_files")

@app.route("/")
def home():
    if not os.path.exists(FILES_DIR):
        return "Files directory not found", 500

    files = os.listdir(FILES_DIR)
    return render_template("index.html", files=files)

@app.route("/files/<path:filename>")
def download_file(filename):
    file_path = os.path.join(FILES_DIR, filename)

    if not os.path.isfile(file_path):
        abort(404)

    return send_from_directory(FILES_DIR, filename, as_attachment=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
