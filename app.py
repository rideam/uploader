from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return 'No file part'
    files = request.files.getlist('files[]')
    if len(files) == 0:
        return 'No selected file'
    for file in files:
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))
    return 'Files uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
