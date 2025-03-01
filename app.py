from flask import Flask, redirect, render_template, request, jsonify, make_response, url_for
from ultralytics import YOLO
import os
import tempfile
import urllib.parse
import cv2
import base64
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

def get_locale():
    return request.cookies.get('lang', 'en')

babel = Babel(app, locale_selector=get_locale)

# Load models
models = {
    'osmf': YOLO('best.pt', task="classify"),
    'calculus_class': YOLO('calculus.pt', task="classify"),
    'calculus_inst': YOLO('calculus-inst.pt', task="segment"),
    'gingivitis': YOLO('gingivitis.pt', task="classify"),
    'phenotype': YOLO('phenotype.pt', task="classify")
}

@app.route('/')
def home():
    return render_template('welcome.html', active_step=0)

@app.route('/set_language/<lang>')
def set_language(lang):
    supported_languages = ['en', 'hi', 'mr']
    if lang not in supported_languages:
        lang = 'en'
    # Redirect to form page after language is selected.
    resp = make_response(redirect(url_for('handle_form')))
    resp.set_cookie('lang', lang)
    return resp

@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'GET':
        return render_template('form.html', active_step=1)
    # Handle form submission (saving patient information in cookies).
    form_data = {
        'name': request.form.get('name'),
        'age': request.form.get('age'),
        'gender': request.form.get('gender'),
        'village': request.form.get('village')
    }
    resp = make_response(redirect(url_for('handle_screening')))
    for key, value in form_data.items():
        resp.set_cookie(key, value)
    return resp

@app.route('/screen', methods=['GET', 'POST'])
def handle_screening():
    if request.method == 'POST':
        selected_diseases = request.form.getlist('diseases')
        resp = make_response(redirect(url_for('upload_screen')))
        resp.set_cookie('diseases', ','.join(selected_diseases))
        return resp
    return render_template('disease_selection.html', active_step=2)

@app.route('/upload')
def upload_screen():
    return render_template('upload.html', active_step=3)

@app.route('/predict', methods=['POST'])
def predict():
    user_data = {key: request.cookies.get(key) for key in ['name', 'age', 'gender', 'village']}
    selected_diseases = request.cookies.get('diseases', '').split(',')
    file = request.files.get('image')
    results = {}

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            file.save(temp_file.name)
            temp_path = temp_file.name

        img = cv2.imread(temp_path)  # Read image in BGR
        if img is None:
            raise ValueError("Could not read the uploaded image")

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB for model processing
        img_annotated = img.copy()  # BGR copy for annotations
        y_position = 30  # Y-coordinate for text

        for disease in selected_diseases:
            model = models.get(disease)
            if not model:
                results[disease] = "NA"
                continue

            if disease == 'calculus_inst':
                # Process segmentation on RGB image
                prediction = model(img_rgb)
                annotated_img_rgb = prediction[0].plot()  # Get RGB annotated image
                annotated_img_bgr = cv2.cvtColor(annotated_img_rgb, cv2.COLOR_RGB2BGR)
                img_annotated = annotated_img_bgr
                results[disease] = str(len(prediction[0].boxes)) if prediction[0].boxes else "0"
            else:
                # Process classification on RGB image
                prediction = model(img_rgb)
                if disease in ['osmf', 'calculus_class', 'gingivitis', 'phenotype']:
                    probs = prediction[0].probs
                    top1 = probs.top1
                    conf = probs.top1conf.item()
                    class_name = model.names[top1]
                    results[disease] = f"{conf*100:.2f}%"
                    # Add text to BGR annotated image
                    label = f"{disease}: {class_name} ({conf*100:.2f}%)"
                    cv2.putText(img_annotated, label, (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    y_position += 30

        # Encode annotated image to base64
        _, buffer = cv2.imencode('.jpg', img_annotated)
        img_base64 = base64.b64encode(buffer).decode('utf-8')

        # Generate Google Form URL
        base_url = "https://docs.google.com/forms/d/e/1FAIpQLSdvPfVMHngCXbGnard4GP9Yn0lKZkcY2XvHlXRxZJHKnLOaXg/formResponse"
        params = {
            'entry.102932375': user_data.get('name', ''),
            'entry.1827218241': user_data.get('age', ''),
            'entry.275491612': user_data.get('gender', ''),
            'entry.609662349': user_data.get('village', ''),
            'entry.1696457345': results.get('osmf', 'NA'),
            'entry.565668057': results.get('calculus_class', 'NA'),
            'entry.656563074': results.get('calculus_inst', 'NA'),
            'entry.1156830156': results.get('gingivitis', 'NA'),
            'entry.1830234866': results.get('phenotype', 'NA'),
            'submit': 'Submit'
        }
        form_url = f"{base_url}?{urllib.parse.urlencode(params)}"

        return jsonify({
            'status': 'success',
            'results': results,
            'form_submission_url': form_url,
            'annotated_image': img_base64
        })

    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 500

    finally:
        if 'temp_path' in locals():
            try:
                os.unlink(temp_path)
            except Exception:
                pass

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)