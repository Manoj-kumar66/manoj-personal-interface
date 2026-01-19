from flask import Flask, render_template
import os

app = Flask(__name__)

FILES_DIR = "my_files"

@app.route("/")
def home():
    files = os.listdir(FILES_DIR)
    return render_template("index.html", files=files)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
