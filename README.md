# OcanPredict - Smart Web Based Application for Dental Disease Detection using Artificial Intelligence

## Overview

OcanPredict is a smart web-based application designed for early screening of OSMF (Oral submucous fibrosis)—a precancerous condition—and various other dental diseases using state-of-the-art machine learning models. This tool leverages computer vision techniques to analyze images submitted via the web interface, offering users a preliminary assessment that can facilitate timely consultation with dental professionals. While it does not replace professional diagnosis, OcanPredict empowers users with an accessible, informative screening process.

The application is multilingual, supporting English, Hindi, and Marathi for local adaptation.

## Demo

Experience the live demo here:
https://huggingface.co/spaces/piyush3/OcanPredict

## Project Structure

Below is the current project structure:
'''
OcanPredict/
├── app.py                      # Main application entry point (e.g., using Flask)
├── best.pt                     # Pre-trained model weights for AI predictions
├── Demo_video.mp4              # Demonstration video showcasing the application
├── Dockerfile                  # Docker configuration for containerization
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── static/
│   └── style.css               # CSS file for static assets
└── templates/
    └── index.html              # HTML template for the web interface
'''

## Installation & Setup

Follow these steps to get the project running locally:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/OcanPredict.git
```

2. Change to the project directory:

```bash
cd OcanPredict
```

3. (Optional) Set up a virtual environment:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python app.py
```

### Running with Docker

Alternatively, you can run the application using Docker:

1. Build the Docker image:

```bash
docker build -t ocanpredict .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 ocanpredict
```

## Features

### Core Functionalities

- Early screening for Oral submucous fibrosis (OSMF) and other dental diseases.
- Real-time image analysis using a pre-trained model (best.pt).
- User-friendly web interface for image submission and results display.
- Multilingual support: English, Hindi, and Marathi.

### User Interface

- Clean, responsive design.
- Intuitive navigation and real-time results visualization.
- Static and templated pages for clear presentation.

## Technical Workflow

1. User accesses the web interface via index.html.
2. An image is captured or uploaded to the application.
3. The AI model (loaded from best.pt) analyzes the image.
4. Processed results along with educational insights are displayed to the user.
5. Additional demonstration resources (e.g., Demo_video.mp4) offer usage guidance.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request on GitHub.

## License

This project is licensed under the MIT License—see the LICENSE file for details.

## Support

For any questions or support, please open an issue in the GitHub repository.

Happy coding!
