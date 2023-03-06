from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop', methods=['POST'])
def crop():
    # Get the uploaded photo and crop parameters from the form
    photo = request.files['photo']
    x = int(request.form['x'])
    y = int(request.form['y'])
    width = int(request.form['width'])
    height = int(request.form['height'])

    # Save the photo to disk
    photo_path = os.path.join(app.root_path, 'static', photo.filename)
    photo.save(photo_path)

    # Open the photo using PIL
    image = Image.open(photo_path)

    # Crop the photo
    cropped_image = image.crop((x, y, x+width, y+height))

    # Save the cropped photo to disk
    cropped_path = os.path.join(app.root_path, 'static', 'cropped_' + photo.filename)
    cropped_image.save(cropped_path)

    # Render the cropped photo
    return render_template('crop.html', photo_path=cropped_path)

if __name__ == '__main__':
    app.run(debug=True)
