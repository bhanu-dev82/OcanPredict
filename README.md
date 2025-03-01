---
title: OcanPredict
emoji: 💻
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
short_description: reserved# OcanPredict - Smart Web Based Application for Dental Disease Detection using Artificial Intelligence

## Overview
OcanPredict is a smart web-based application designed for early screening OSMF (Oral submucous fibrosis) which is a precancerous condition. It can also screen for various dental diseases using the power of Artificial Intelligence. It leverages state-of-the-art machine learning models and computer vision techniques to analyze real-time camera input and provide users with preliminary assessments of several oral health conditions. This tool aims to empower individuals with accessible and convenient preliminary screenings, promoting proactive dental care and early intervention. While not a replacement for professional diagnosis, OcanPredict can serve as an informative tool for raising awareness and encouraging timely consultations with dental professionals

Also It is multilingual supporting English, Hindi and Marathi for local adaptation. 

## Demo
https://huggingface.co/spaces/piyush3/OcanPredict

## Tech Stack & Tools

### Frontend
- React.js
- Vite
- TailwindCSS
- TensorFlow.js
- MediaPipe

### Development Tools
- Node.js
- npm/yarn
- Git & GitHub

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/OcanPredict-master.git
```

```bash
cd OcanPredict-master
```

```bash
npm install
```

```bash
npm run dev
```

## Features

### Core Functionalities
- Real-time facial analysis using TensorFlow.js
- Multiple condition assessment:
  - Oral Cancer Detection
  - Gingivitis Analysis
  - Calculus Detection
  - OSMF Assessment
  - Caries Detection
  - Phenotype Analysis

### User Interface
- Responsive design
- Intuitive navigation
- Real-time camera integration
- Detailed results visualization
- Educational information section

## Project Structure

```
OcanPredict/
├── src/                  # Source files
│   ├── components/      # Reusable UI components
│   ├── Pages/          # Main application pages
│   └── assets/         # Static resources
├── public/             # Public assets and models
│   └── models/        # ML models
└── dist/              # Production build
```

## Technical Workflow

1. **User Interface Layer**
   - React components handle the UI rendering
   - TailwindCSS manages styling
   - Vite provides fast development and optimization

2. **ML Processing Layer**
   - TensorFlow.js loads and runs ML models
   - Face detection using MediaPipe
   - Real-time analysis and prediction

3. **Data Flow**
   - Camera input → Face Detection → Feature Extraction → Analysis → Results

## Development Setup

1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

For more information or support, please open an issue in the GitHub repository.

---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
