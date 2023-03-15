from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from PIL import Image

UPLOAD_FOLDER = '/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/Utveckling av webbapplikationer/Flask/flask projekt/static/upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upl():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      name = secure_filename(f.filename)
      complete_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
      f.save(complete_path)
      im = Image.open(complete_path)

      return render_template(
         'file.html', 
         name = name,
         filename = 'upload/'+name, 
         filetype = f.headers['Content-Type'],
         fileformat = im.size,
         filesize = os.path.getsize(complete_path),
         filepath = complete_path
         )

if __name__ == '__main__':
   app.run(debug = True)
