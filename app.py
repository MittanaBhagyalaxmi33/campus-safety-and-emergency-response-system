from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload-video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video uploaded'}), 400

    video = request.files['video']
    filepath = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(filepath)

    if os.path.getsize(filepath) > 3 * 1024 * 1024:
        crowd_detected = True
    else:
        crowd_detected = False

    return jsonify({'crowd_detected': crowd_detected})

