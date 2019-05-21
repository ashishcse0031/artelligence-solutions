# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify,render_template
import pickle

app = Flask(__name__)

# Load the model
model = None#pickle.load(open('model.pkl','rb'))

@app.route('/')
def root():
	return render_template('index.html')
	
if __name__ == '__main__':
    app.run(port=5050, debug=True)
