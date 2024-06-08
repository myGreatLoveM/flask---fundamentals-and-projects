from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os

app = Flask(__name__)

app.config['UPLOAD_DIRECTORY'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']

@app.route('/')
def home():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    images = []

    for file in files:
        extension = os.path.splitext(file)[1].lower()
        if extension in app.config['ALLOWED_EXTENSIONS']:
            images.append(file)
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    try: 
        file = request.files.get('file')

        os.makedirs(os.path.join(os.getcwd(), 'uploads'), exist_ok=True)

        if file:
            extension = os.path.splitext(file.filename)[1].lower()
            if extension not in app.config['ALLOWED_EXTENSIONS']:
                return 'File is not allowed to upload, please upload image only '
            file.save(os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename(file.filename)))
    except RequestEntityTooLarge:
        return 'File is larger than allowed limits, file size should be below 16MBs'
    return redirect('/')

@app.route('/serve_image/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_DIRECTORY'], filename)

if __name__ == '__main__':
    app.run(debug=True) 