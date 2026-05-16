from flask import Flask, render_template, request
import os
import PyPDF2

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload_file():

    if 'resume' not in request.files:
        return "No file uploaded"

    file = request.files['resume']

    if file.filename == '':
        return "No file selected"

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    text = ""

    with open(filepath, 'rb') as pdf_file:

        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    skills = [
        "python",
        "java",
        "sql",
        "html",
        "css",
        "javascript",
        "mysql",
        "flask",
        "react",
        "machine learning",
        "power bi",
        "excel"
    ]

    detected = []

    for skill in skills:
        if skill.lower() in text.lower():
            detected.append(skill)

    score = int(
        (len(detected)/len(skills))*100
    )

    if score >= 80:
        feedback = "Excellent ATS compatibility"
        suggestions = [
            "Resume contains strong technical keywords",
            "Good skill coverage",
            "Maintain clean formatting"
        ]

    elif score >= 50:
        feedback = "Average ATS compatibility"

        suggestions = [
            "Add more technical skills",
            "Include projects",
            "Use stronger keywords"
        ]

    else:

        feedback = "Low ATS compatibility"

        suggestions = [
            "Add skills section",
            "Mention projects",
            "Use role-specific keywords"
        ]

    return render_template(
        "result.html",
        score=score,
        feedback=feedback,
        suggestions=suggestions
    )


if __name__=="__main__":
    app.run(debug=True)