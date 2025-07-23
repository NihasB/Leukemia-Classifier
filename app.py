from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os


app = Flask(__name__)
print("Current working directory:", os.getcwd())
model = load_model('N:/LEUKEMIA CELL CLASSIFICATION/Model/final_model.h5')# Load your trained model

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CLASS_NAMES = ['Leukemia', 'Normal']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded!", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected!", 400

    # ✅ Ensure the upload folder exists before saving
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filepath)

    img = image.load_img(filepath, target_size=(64, 64))
    img_tensor = image.img_to_array(img) / 255.0
    img_tensor = np.expand_dims(img_tensor, axis=0)

    prediction = model.predict(img_tensor)
    predicted_class = CLASS_NAMES[int(prediction[0] > 0.5)]

    return render_template('result.html', image_path=filepath, prediction=predicted_class)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
