<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OSMF Detection</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1>OSMF Classification : OcanPredict</h1>
        
        <div class="main-content">
            <div class="left-panel">
                <div class="upload-section">
                    <h2>Upload Image</h2>
                    <div class="file-upload">
                        <input type="file" id="fileInput" accept="image/*">
                        <label for="fileInput">Choose File</label>
                    </div>
                    <button id="uploadPredict" disabled>Analyze Upload</button>
                </div>

                <div class="separator">
                    <span>OR</span>
                </div>

                <div class="camera-section">
                    <h2>Capture Image</h2>
                    <video id="video" autoplay playsinline></video>
                    <canvas id="canvas" style="display: none;"></canvas>
                    <button id="capture">Capture Image</button>
                </div>
            </div>

            <div class="right-panel">
                <div class="preview-section">
                    <h2>Preview</h2>
                    <img id="preview" style="display: none;">
                    <button id="predict" disabled>Analyze Capture</button>
                </div>
                <div id="result" class="result-container"></div>
            </div>
        </div>
    </div>
    <script>
        const video = document.getElementById('video');
        const canvas = document.getElementById('canvas');
        const preview = document.getElementById('preview');
        const captureBtn = document.getElementById('capture');
        const predictBtn = document.getElementById('predict');
        const result = document.getElementById('result');
        const fileInput = document.getElementById('fileInput');
        const uploadPredict = document.getElementById('uploadPredict');

        // Access webcam
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
            });

        // File upload handling
        fileInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                    uploadPredict.disabled = false;
                    predictBtn.disabled = true;
                };
                reader.readAsDataURL(file);
            }
        });

        captureBtn.addEventListener('click', () => {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            
            preview.src = canvas.toDataURL('image/png');
            preview.style.display = 'block';
            predictBtn.disabled = false;
            uploadPredict.disabled = true;
            fileInput.value = '';
        });

        async function predict(formData) {
            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                
                result.innerHTML = `
                    <h2>Results:</h2>
                    <p>Classification: ${data.class}</p>
                `;
            } catch (error) {
                result.innerHTML = 'Error during prediction';
            }
        }

        predictBtn.addEventListener('click', async () => {
            const blob = await (await fetch(preview.src)).blob();
            const formData = new FormData();
            formData.append('image', blob, 'capture.png');
            await predict(formData);
        });

        uploadPredict.addEventListener('click', async () => {
            const formData = new FormData();
            formData.append('image', fileInput.files[0]);
            await predict(formData);
        });
    </script>
</body>
</html>
