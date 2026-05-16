# Smart Resume Analyzer with ATS Scoring

## Overview
Smart Resume Analyzer is a Flask-based web application that helps users evaluate resumes through automated analysis. Users can upload a PDF resume and receive an ATS score, feedback, and improvement suggestions.

## Features
- Upload PDF resumes
- Resume text extraction using PyPDF2
- Skill detection from resume content
- ATS score calculation
- Feedback generation
- Suggestions for resume improvement
- Modern responsive UI

## Technologies Used
- Python
- Flask
- HTML
- CSS
- PyPDF2
- Gunicorn

## Project Structure

Resume-Analyzer
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates
│   ├── index.html
│   └── result.html
│
├── static
│   └── style.css
│
└── uploads

## Installation

1. Clone repository

git clone https://github.com/patlollaraghavi799/Resume-Analyzer.git

2. Move into project folder

cd Resume-Analyzer

3. Install dependencies

pip install -r requirements.txt

4. Run application

python app.py

5. Open browser

http://127.0.0.1:5000

## How It Works

1. User uploads a PDF resume
2. Resume text is extracted
3. Technical skills are identified
4. ATS score is calculated
5. Feedback and suggestions are generated

## Future Enhancements
- NLP based skill extraction
- Job description matching
- AI-powered recommendations
- Advanced ATS analysis

## Author
Patlolla Raghavi