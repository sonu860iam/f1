# app.py
from flask import Flask, request, jsonify
from model import get_prediction, get_image_description

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify_image():
    data = request.get_json()
    url = data['url']
    prediction = get_prediction(url)
    objects, description = get_image_description(prediction)
    return jsonify({'objects': objects, 'description': description})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
