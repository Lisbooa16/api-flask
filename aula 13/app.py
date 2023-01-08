from flask import Flask, redirect, request, render_template, session, url_for, send_file
import os
from pathlib import Path
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')
upload_folder = os.path.join(os.getcwd(), 'upload')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    savepath = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(savepath)
    return 'upload feito com sucesso'


@app.route('/get-file/<filename>')
def getfile(filename):
    file = os.path.join(upload_folder, filename + '.png')
    return send_file(file, mimetype="imagem/png")



if __name__ == '__main__':
    app.run(debug=True, port='3000')