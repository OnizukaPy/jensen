# File: app.py
# importering av moduler

from flask import Flask, render_template, request     # flask modulen för att skapa webbapplikationer
from werkzeug.utils import secure_filename            # werkzeug modulen för att hantera filer
import os                                             # os modulen för att hantera filsystemet
from PIL import Image                                 # PIL modulen för att hantera bilder och få bildens informationer

# Konstanter
# mappen där filerna ska sparas
UPLOAD_FOLDER = '/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/Utveckling av webbapplikationer/Flask/flask projekt/static/upload'

# Flask applikationen
app = Flask(__name__)

# konfigurering av applikationen
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Flask routes
# route för att visa formuläret
@app.route('/')
def upl():
   # returnera formuläret med hjälp av template filen upload.html
   # som ligger i mappen templates
   return render_template('upload.html')

# route för att analisera uppladdningen av filen
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      name = secure_filename(f.filename)
      complete_path = os.path.join(app.config['UPLOAD_FOLDER'], name)   # sökvägen till filen skapas med hjälp av os modulen
      f.save(complete_path)
      im = Image.open(complete_path)

      # returnera resultatet av analysen med hjälp av template filen file.html 
      # som ligger i mappen templates
      return render_template(
         'file.html', 
         name = name,
         filename = 'upload/'+name, 
         filetype = f.headers['Content-Type'],        # filtypen är i headers diktionäret med nyckeln 'Content-Type'
         fileformat = im.size,                        # bildens storlek är i size attributet i Image objektet
         filesize = os.path.getsize(complete_path),   # filens storlek får vi med hjälp av os modulen
         filepath = complete_path
         )

# starta applikationen och sätt debug till True
if __name__ == '__main__':
   app.run(debug = True)
