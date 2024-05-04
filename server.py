from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import slicer

# CHANGE ME TO YOUR GCODE PATH
EXPORT_PATH = 'CHANGE ME TO YOUR GCODE PATH'
# ex: EXPORT_PATH = '/home/username/printer_data/gcodes'

app = Flask(__name__)
UPLOAD_FOLDER = 'tmp'
CONFIG_FILE = 'configs/config.ini'
@app.route("/")
def main():
    return render_template("slice.html")


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
        if slicer.slice_to_gcode(os.path.join(EXPORT_PATH,file_secure_name+".gcode"), file_path, CONFIG_FILE).returncode == 0:
            os.remove(file_path)
            return render_template("success.html")
        else:
            os.remove(file_path)
            return render_template("error.html")
