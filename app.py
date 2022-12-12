# importing necessary libraries and functions
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sklearn

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb')) # loading the trained model

@app.route('/',methods=['GET']) # Homepage
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type = request.form['Fuel_Type']
        Age_of_the_Car = request.form['Age_of_the_Car']
        Seller_Type=request.form['Seller_Type']
        Transmission=request.form['Transmission']
    
    
    prediction = model.predict([[Present_Price,Kms_Driven,Owner,Fuel_Type,Age_of_the_Car,Seller_Type,Transmission]]) # making prediction

    output=round(prediction[0],2)
    return render_template('index.html', prediction_text="You can sell your car at {} lakhs".format(output)) # rendering the predicted result

if __name__ == "__main__":
    app.run(debug=True)