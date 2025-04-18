from flask import Flask, request, render_template, url_for,jsonify,send_file
from werkzeug.utils import secure_filename
from pdf2docx import Converter
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['pdf_file']
        if file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            unique_id = str(uuid.uuid4())
            input_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}.pdf")
            output_path = os.path.join(CONVERTED_FOLDER, f"{unique_id}.docx")
            
            file.save(input_path)

            # Convert PDF to Word
            cv = Converter(input_path)
            cv.convert(output_path, start=0, end=None)
            cv.close()

            # ✅ Return JSON instead of redirect
            download_url = url_for('download_file', filename=f"{unique_id}.docx", _external=True)
            return jsonify({'download_url': download_url})
        else:
            return jsonify({'error': 'Invalid file type. Only PDFs allowed.'}), 400

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(CONVERTED_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
