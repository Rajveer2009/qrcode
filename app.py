import qrcode
import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/<data>', methods=['GET', 'POST'])
def main(data):
    img = qrcode.make(data)
    img_path = os.path.join('static', f'{data}.png')
    img.save(img_path)
    try:
        return send_file(img_path, mimetype='image/png', as_attachment=True)
    finally:
        os.remove(img_path)
   
