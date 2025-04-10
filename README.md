🦷 Dental X-ray Abnormality Detection App
An AI-powered full-stack web application to detect potential abnormalities in dental X-rays using unsupervised deep learning (Convolutional Autoencoders).

🚀 Live Demo
🔗 (https://dental-abnormality-test.onrender.com)

📌 Features
Upload dental X-ray images via web UI

Model reconstructs image and calculates anomaly score

Flags image as Normal or Abnormal

Simple, fast, and effective for early screening

🧠 ML Model
Type: Convolutional Autoencoder

Input: Grayscale 128×128 X-ray images

Output: Reconstructed image

Anomaly Detection: Based on reconstruction error threshold

🛠️ Tech Stack
Model: TensorFlow / Keras

Backend: Flask (Python)

Frontend: HTML + JS

Deployment: Render (Free Tier)

Storage: Model loaded from disk (.keras)

📁 Folder Structure
swift
Copy
Edit
/DentalXrayApp/
├── app.py
├── index.html
├── autoencoder_model.keras
├── requirements.txt
├── render.yaml
▶️ How to Run Locally
Clone the repo:

bash
Copy
Edit
git clone https://github.com/Navin0305/Dental_Abnormality_Test.git
cd Dental_Abnormality_Test
Create environment and install:

bash
Copy
Edit
pip install -r requirements.txt
Run:

bash
Copy
Edit
python app.py
Then open http://127.0.0.1:5000/ in your browser.

🌐 How to Deploy on Render
Push project to GitHub

Go to https://render.com

Create new web service → link your repo

Build command: pip install -r requirements.txt

Start command: python app.py

Add app.run(host="0.0.0.0", port=10000) to app.py

👨‍👩‍👧‍👦 Team Members
Navin Suresh – Model training, Flask API, project lead

Shijin Joseph – Frontend UI/UX, deployment

Neethu Jose – Preprocessing, evaluation, demo video & documentation
