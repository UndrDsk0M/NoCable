from flask import Flask, request, send_from_directory, render_template, redirect, url_for, make_response
from datetime import datetime, timedelta
import sched, time, threading
import sched, time
import threading
import string
import socket
import random
import base64
import segno
import os

app = Flask(__name__)

# setting a scheduler for auto deleting files after 5min
scheduler = sched.scheduler(time.time, time.sleep)

# setting the uploads folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



def delete_file_auto(file_path):
    os.remove(file_path)
    
def auto_deleter_handler(filepath):
    scheduler.enter(300, 1, delete_file_auto, argument=(filepath,))
    scheduler.run()
    
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "0.0.0.0"
    finally:
        s.close()

port = "3000"

@app.route('/')
def index():
    ip = get_ip()
    qr = segno.make(f'http://{ip}:{port}')
    qr.save("./static/img/qrcode.png")
    
    files = list(os.listdir(UPLOAD_FOLDER))
    files.reverse()
    print(files)
    return render_template('index.html', qrcode=f'http://{ip}:{port}', files=files)


@app.route('/message', methods=['POST'])
def message():
    text = request.form['text']
    print(text)
    if text == "":
        return "no message", 400
    try :
        file_name:str = text[0:10].replace(" ", "_") + str(datetime.now())
    except: 
        file_name:str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    with open(f"uploads/{file_name}.text", 'w') as pen:
        pen.write(text)

    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file:str = request.files['file']
    filepath:str = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    threading.Thread(target=auto_deleter_handler, daemon=True, args=(filepath, )).start()
    return "200"

@app.route('/download/<filename>')
def download_file(filename):
    filepath:str = os.path.join(UPLOAD_FOLDER, filename)
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):

    filepath:str = os.path.join(UPLOAD_FOLDER, filename)
    try:
        os.remove(filepath)
    except Exception as e:
        return e, 404
    return redirect(url_for('index'))


if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=port)
