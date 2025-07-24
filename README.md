# Leukemia-Classifier
Leukemia Cell Classification Using Deep Learning

This project is a web-based deep learning system for classifying blood cell images as either normal (HEM) or leukemic (ALL) using a Convolutional Neural Network (CNN).

##  Objective

To help medical professionals detect leukemia by analyzing microscopic blood cell images using an automated AI-based classification system.

---

##  Tech Stack

| Technology             | Purpose                                   |
|------------------------|-------------------------------------------|
| **Python**             | Core programming language                 |
| **TensorFlow & Keras** | Building and training the CNN model       |
| **Flask**              | Web app framework                         |
| **HTML/CSS**           | Frontend for file upload & result display |
| **NumPy, OpenCV**      | Image processing & array operations       |
| **Jinja2**             | HTML templating in Flask                  |

---

##  Project Structure

├── Notebooks/
│   └── leukemia_classification.ipynb  # Main Jupyter notebook
├── Model/
│   ├── best_model.h5                  # Best model during training
│   └── final_model.h5                 # Final trained model
├── static/
│   ├── uploads/                       # User-uploaded images
│   └── style.css                      # Web interface styling
├── templates/
│   ├── index.html                     # Upload page
│   └── result.html                    # Results page
├── Data/
│   ├── Train_data/
│   │   ├── Lukemia/                   # Training leukemia images
│   │   └── Normal/                    # Training normal images
│   └── Test_data/
│       ├── Lukemia/                   # Test leukemia images
│       └── Normal/                    # Test normal images
├── app.py                             # Flask web application
└── requirements.txt                   # Python dependencies
---

##  Sample Images

| Normal Cell (HEM) | Leukemia Cell (ALL) |
|-------------------|---------------------|
| ![Normal](static/samples/hem.jpg) | ![ALL](static/samples/all.jpg) |

---

💡 How It Works

Users upload a blood cell image via the web interface.

The image is preprocessed and passed into a CNN model.

The model returns whether the cell is HEM (normal) or ALL (leukemia).

The result is displayed on the webpage with the uploaded image.


Challenges Faced

Preprocessing varied image types and sizes

Handling model file size for deployment

Designing a user-friendly interface

Integrating model with Flask without latency


📄 License
This project is open-source and available under the MIT License.

🤝 Acknowledgements
Dataset: ALL-IDB