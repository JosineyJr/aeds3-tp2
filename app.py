from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from file.file import compress_file, decompress_file

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads/"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compress", methods=["GET", "POST"])
def compress():
    if request.method == "POST":
        f = request.files["file"]
        filename = secure_filename(f.filename)
        if filename.endswith(".txt"):
            filename = filename[:-4]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        f.save(filepath + ".txt")
        compress_file(filepath + ".txt", filepath + ".huf")
        return render_template("compress.html", filename=filename + ".huf")
    return render_template("compress.html")


@app.route("/decompress", methods=["GET", "POST"])
def decompress():
    if request.method == "POST":
        f = request.files["file"]
        filename = secure_filename(f.filename)
        if filename.endswith(".huf"):
            filename = filename[:-4]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        f.save(filepath + ".huf")
        decompress_file(filepath + ".huf", filepath + ".txt")
        return render_template("decompress.html", filename=filename + ".txt")
    return render_template("decompress.html")


if __name__ == "__main__":
    app.run(debug=True)
