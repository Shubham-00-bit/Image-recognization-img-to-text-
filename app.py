from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import ollama

app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            
            result = process_image(filepath)
            return render_template('index.html', uploaded_image=file.filename, result=result)
    return render_template('index.html')

def process_image(image_path):
    
    res = ollama.chat(
        model='llava',
        messages=[
            {'role': 'user', 'content': 'Describe this image', 'image': image_path}
        ]
    )
    return res.get('message', {}).get('content', 'No description available.')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

