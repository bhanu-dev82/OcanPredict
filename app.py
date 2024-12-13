from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
import os
import tempfile
import base64
import json

app = Flask(__name__)

# Load OSMF model
osmf = YOLO('best.pt', task="classify")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})
    
    file = request.files['image']
    
    try:
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            file.save(temp_file.name)
            temp_path = temp_file.name
        
        # Process image
        predict = osmf(temp_path)
        results = predict[0].to_json()  # Using the new recommended method
        predict_dict = json.loads(results)
        
        name = predict_dict[0]["name"]
        confidence = float(predict_dict[0]["confidence"]) * 100
        
        # Close file handle and remove
        try:
            os.close(temp_file.fileno())
        except:
            pass
        
        try:
            os.unlink(temp_path)
        except:
            pass
            
        return jsonify({
            'class': name,
            'confidence': f"{confidence:.2f}%",
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
