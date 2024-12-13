from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
import os
import tempfile
import base64
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure maximum content length for file uploads (10MB)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# Load OSMF model
model_path = os.getenv('MODEL_PATH', 'best.pt')
osmf = YOLO(model_path, task="classify")

@app.route('/')
def home():
return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
if 'image' not in request.files:
return jsonify({'error': 'No image provided', 'status': 'error'}), 400

file = request.files['image']
if not file.filename:
return jsonify({'error': 'Empty file provided', 'status': 'error'}), 400

try:
# Secure the filename and create temporary file
filename = secure_filename(file.filename)
with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
file.save(temp_file.name)
temp_path = temp_file.name

# Process image
predict = osmf(temp_path)
results = predict[0].to_json()
predict_dict = json.loads(results)

# Extract prediction results
name = predict_dict[0]["name"]
confidence = float(predict_dict[0]["confidence"]) * 100

except Exception as e:
return jsonify({
'error': str(e),
'status': 'error'
}), 500

finally:
# Cleanup temporary files
try:
if 'temp_file' in locals():
os.close(temp_file.fileno())
os.unlink(temp_path)
except Exception:
pass

return jsonify({
'class': name,
'confidence': f"{confidence:.2f}%",
'status': 'success'
})

if __name__ == '__main__':
port = int(os.environ.get('PORT', 7860))
app.run(host='0.0.0.0', port=port)