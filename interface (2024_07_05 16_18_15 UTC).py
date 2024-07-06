from flask import Flask, request, jsonify
from PIL import Image
import numpy as np

app = Flask(__name__)

class Interface:
    def __init__(self):
        self.app = app

    def run(self, debug=False):
        self.app.run(debug=debug)

    @app.route("/process_image", methods=["POST"])
    def process_image():
        image_url = request.json["url"]
        # Load the image using PIL
        image = Image.open(image_url)
        # Pre-process the image
        image = np.array(image)
        # Run the image through the model
        objects, description = model.process_image(image)
        # Return the output in the required format
        output = {
            "objects": objects,
            "description": description
        }
        return jsonify(output)
