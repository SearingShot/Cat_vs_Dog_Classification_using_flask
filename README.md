# Cat vs Dog Classifier

This Flask application is designed to classify images as either cats or dogs using a convolutional neural network model. Users can upload images through the provided interface, and the application will display whether the image contains a cat or a dog.

## Setup Instructions

1. **Clone the Repository:** Clone this repository to your local machine.

    ```bash
    git clone https://github.com/SearingShot/Cat_vs_Dog_Classification_using_flask.git
    ```

2. **Install Dependencies:** Install all the required Python libraries using pip.

3. **Download the Dataset:** Get The Dataset from here :- [Data](https://github.com/laxmimerit/dog-cat-full-dataset.git)

4. **Train the Model:** Before running the Flask app, you need to train the model by executing the Train.py script. This script will generate the model file (model.h5) required for classification.

5. **Run the Flask App:** Execute the main.py file to start the Flask application.

6. **Access the Web Application:** Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the application.

## Usage Instructions

1. **Upload Image:** Click on the "Choose File" button to select an image file from your local machine.

2. **Submit Image:** After selecting the image file, click on the "Predict" button to upload the image to the application.

3. **View Result:** Once the prediction is completed, the application will display whether the uploaded image contains a cat or a dog.

## Folder Structure

- **uploads:** This folder stores the uploaded image files.
- **templates:** Contains HTML templates for rendering the web pages.
- **main.py:** Python script to run the Flask application.
- **Train.py:** Python script to train the model using image data.
- **model.h5:** A deep learning model for image classification which will be created after running Train.py.

## Requirements

- Python 3.x
- Flask
- OpenCV
- NumPy
- TensorFlow
- Keras

## Notes

- The model file (model.h5) is generated after running the Train.py script. You can modify the training parameters in Train.py to customize the model.
- You can replace the model file (model.h5) with your custom-trained model if needed.

## Results
- Choosing Image

![Choose Image](https://github.com/SearingShot/Cat_vs_Dog_Classification_using_flask/assets/121299642/8c38db5e-0ada-4f70-bb59-77b952013433)


- Selecting the Image

![Selecting The Image](https://github.com/SearingShot/Cat_vs_Dog_Classification_using_flask/assets/121299642/c8b622cb-a7f4-4e0f-803a-60bdb6c6ed04)


- Result

![Result](https://github.com/SearingShot/Cat_vs_Dog_Classification_using_flask/assets/121299642/ba4e94be-80c7-40fa-867b-a015cdbcec7b)


