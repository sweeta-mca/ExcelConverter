import os
from flask import Flask, flash, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
from convert import Converter


UPLOAD_FOLDER = 'D:/Chola_work/file_upload'
ENCODED_FOLDER ='D:/Chola_work/file_upload/encoded'
DECODED_FOLDER = 'D:/Chola_work/file_upload/decoded'


ALLOWED_EXTENSIONS = {'csv','xlsx','xls'}

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ENCODED_FOLDER'] = ENCODED_FOLDER
app.config['DECODED_FOLDER'] = DECODED_FOLDER

con = Converter.Converter.getInstance()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Encoded</h1>"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/download', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':            
        filename = request.form['filename']                
        if filename == '':
            flash('No file name given')
            return redirect(request.url)  
        if filename and allowed_file(filename):  
            source_path = os.path.join(app.config['ENCODED_FOLDER'], filename)
            destination_path = os.path.join(app.config['DECODED_FOLDER'], filename)
            con.toBase64(source_file_path=source_path,destination_file_path=destination_path)
            return send_from_directory(app.config['DECODED_FOLDER'], filename)
    return '''
    <!doctype html>
    <title>Download a File</title>
    <h1>Download a File</h1>
    <form method=post action="/download">
       <input type="text" name="filename"><br>
      <input type=submit value=download>
    </form>
    '''

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            source_path =os.path.join(app.config['UPLOAD_FOLDER'], filename)
            destination_path = os.path.join(app.config['ENCODED_FOLDER'], filename)
            con.toBase64(source_file_path=source_path,destination_file_path=destination_path)
            #return redirect(url_for('download', name=filename))
            return "File encoded successfully"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run()
