from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('gallery', filename=filename))
    return render_template('index.html')

@app.route('/gallery/<filename>')
def gallery(filename):
    return render_template('gallery.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
