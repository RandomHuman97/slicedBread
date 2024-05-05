from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import slicer
from EDITME import EXPORT_PATH

app = Flask(__name__)
UPLOAD_FOLDER = 'tmp'
configs = []

# fetch configs
for filename in os.listdir("configs"):
    if filename.endswith(".ini"):
        configs.append(filename)
@app.route("/")
def main():
    return render_template("slice.html", configs=configs)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename == '':
            return render_template("error.html")
        if f.filename.split('.')[-1] != 'stl':
            return render_template("error.html")
        file_secure_name = secure_filename(f.filename)
        file_path = os.path.join(UPLOAD_FOLDER, file_secure_name)
        f.save(file_path)
        if slicer.slice_to_gcode(os.path.join(EXPORT_PATH, file_secure_name + ".gcode"), file_path,
                                 os.path.join("configs", request.form['Config'])).returncode == 0:
            os.remove(file_path)
            return render_template("success.html")
        else:
            os.remove(file_path)
            return render_template("error.html")
    return render_template("error.html")