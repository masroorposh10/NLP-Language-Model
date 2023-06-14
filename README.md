# NLP Language Checker
This project implements a Natural Language Processing (NLP) model that can detect the language of a given input text. It uses a pre-trained language detection model to predict the language of the input text.

# Prerequisites
Python 3.6 or above
Required packages: pickle, string, streamlit, webbrowser
# Installation
Clone the repository or download the project files.
Install the required packages by running the following command:
Copy code
pip install -r requirements.txt
# Usage
Ensure that you have the following files in the project directory:
model.pckl: A pickled language detection model file.
Run the script by executing the following command:
arduino

streamlit run app.py
Access the application in your web browser using the provided local URL.
# User Interface
The application provides a simple web interface where you can input a text and get the predicted language of that text. It follows these steps:

Enter your input text in the provided text input field.
Click the "Click to get Language" button.
The predicted language will be displayed below the button.
# Model Details
The language detection model used in this project is stored in the model.pckl file. It has been pre-trained on a labeled dataset containing various languages. The model predicts the language of a given text using its internal classification algorithm.

# Contributing
Contributions to this project are welcome. If you find any issues or want to enhance the functionality, feel free to open a pull request.

# License
This project is licensed under the MIT License.

# Acknowledgments
Special thanks to the creators and contributors of the libraries and tools used in this project.
The dataset this model was trained on:
  https://www.kaggle.com/basilb2s/language-detection
