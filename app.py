from flask import Flask, jsonify, request
import pytesseract as tess
from PIL import Image
from io import BytesIO
import requests

app = Flask(__name__)
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
 
@app.route("/")
def home_view():
    return "<h1>Atrades OCR</h1>"

@app.route("/ocr", methods=["POST"])
def read_text():    
    img_resp = requests.get(request.json["image_url"], stream=True)
    img = Image.open(img_resp.raw)

    text = tess.image_to_string(img)    

    return text

if __name__ == "__main__":
    app.run(debug=True, port=3000 )