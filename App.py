from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import os

# App initialization
app = Flask(__name__, static_url_path='', static_folder='.')

# Load the trained model
model = tf.keras.models.load_model("autoencoder_model.keras")

# Constants
IMG_SIZE = (128, 128)
THRESHOLD = 0.003344  # Adjust this based on your evaluation results

# Preprocess image
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('L')
    img = img.resize(IMG_SIZE)
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=(0, -1))  # Shape: (1, 128, 128, 1)
    return img

# Serve the frontend
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    image = preprocess_image(file.read())
    reconstructed = model.predict(image)
    error = np.mean((image - reconstructed) ** 2)
    status = "Abnormal" if error > THRESHOLD else "Normal"

    return jsonify({
        "status": status,
        "reconstruction_error": float(error)
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=False)
