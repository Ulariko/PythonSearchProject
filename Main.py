# app.py
from flask import Flask, request, render_template
import re
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    highlighted_text = ""
    if request.method == 'POST':
        word = request.form['word']
        file = request.files['file']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        highlighted_text = re.sub(rf'\b{word}\b', f'<mark>{word}</mark>', text, flags=re.IGNORECASE)

    return render_template('index.html', result=highlighted_text)

if __name__ == '__main__':
    app.run(debug=True)
