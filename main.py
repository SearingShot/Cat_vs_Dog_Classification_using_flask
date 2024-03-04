from flask import Flask, request, render_template
import os
import cv2
from keras.models import load_model
import numpy as np
app = Flask(__name__)

## Load the trained model
model = load_model('model.h5')

## Define the function to preprocess the image
def preprocess(img):
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

## Define the prediction function
@app.route('/predict', methods=['POST'])
def predict():
    # Get the file from the request
    file = request.files['image']

    # Save the file to the uploads folder
    file.save(os.path.join('uploads', file.filename))
    
    # Read the image
    img = cv2.imread(os.path.join('uploads', file.filename))
    
    # Preprocess the image
    img = preprocess(img)
    
    # Make predictions
    prediction = model.predict(img)
    if prediction[0] > 0.7:
        return 'Dog'
    else:
        return 'Cat'

## Define the function to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

## Define the main function
if __name__ == '__main__':
    app.run(debug=True)