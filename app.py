from flask import Flask, request, render_template
import os
from __init__ import removeBg  # Import your background removal function

app = Flask(__name__)

@app.route('/remove_background', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No file part'
        image = request.files['image']
        if image.filename == '':
            return 'No selected file'

        if image:
            image_path = os.path.join('uploads', image.filename)
            image.save(image_path)
            result = removeBg(image_path)
             # Serve the background-removed image to the user
            return f'Background Removed: <img src="/static/output/{image.filename}">'

    return render_template('index.html')

# Route to serve the background-removed image
@app.route('/static/output/<filename>')
def serve_output(filename):
    return send_file(f'uploads/{filename}', as_attachment=False)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        
    webbrowser.open('http://127.0.0.1:5000/')

    app.run(debug=True)
