from flask import Flask, request, send_from_directory, render_template, redirect, url_for, make_response
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64

def decrypt_file_data(encrypted_data, password):
    key = SHA256.new(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)  # ساده‌ترین مدل، برای تست فقط!
    decoded = base64.b64decode(encrypted_data)
    decrypted = cipher.decrypt(decoded)
    return decrypted.rstrip(b"\0")  # حذف padding دستی

import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    with open(filepath, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted = decrypt_file_data(encrypted_data, "supersecret")
    
    response = make_response(decrypted)
    response.headers.set('Content-Type', 'application/octet-stream')
    response.headers.set('Content-Disposition', 'attachment', filename=filename.replace(".enc", ""))
    return response

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    try:
        os.remove(filepath)
    except Exception as e:
        return e, 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
