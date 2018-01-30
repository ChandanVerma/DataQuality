import numpy as np
from flask import Flask, abort, jsonify, request
import pickle 
import logging
import json
import csv
from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required
import io
import pandas as pd
#from . import app, estimator, target_names
from preprocessing import *
#random_forest_model = pickle.load(open("rfc.pkl","rb"))
xgb_model = pickle.load(open('D:/Projects/Data_Quality/xgb_model.pkl','rb'))
app = Flask(__name__)
from flask import Flask, render_template, flash, request
from flask_table import Table, Col
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
 
@app.route("/send", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        FIRSTNAME = request.form['FIRSTNAME']
        #print(FIRSTNAME.shape)
        LASTNAME = request.form['LASTNAME']
        GENDERCODE = request.form['GENDERCODE']
        DATEOFBIRTH = request.form['DATEOFBIRTH']
        ETHNICITYCODE = request.form['ETHNICITYCODE']
        RACECODE = request.form['RACECODE']
        MARITALSTATUS = request.form['MARITALSTATUS']
        allvalues = [FIRSTNAME, LASTNAME, GENDERCODE, DATEOFBIRTH, ETHNICITYCODE, RACECODE, MARITALSTATUS]
        print(allvalues)
        #data = np.concatenate([FIRSTNAME, LASTNAME, GENDERCODE, DATEOFBIRTH, ETHNICITYCODE, RACECODE, MARITALSTATUS])
        predict_request = np.array(allvalues).reshape((1,-1))
        print(predict_request)
        y = xgb_model.predict(predict_request)
        print(y)
        output = [y[0]]
        #return jsonify(results=output)
        return render_template('Score.html', score = output)
    return render_template('index.html')	

@app.route('/upload', methods=['POST'])
def predict():
     # Error checking
      data_csv = request.files['inputFile']
      if not data_csv:
          return "No file"
      DQ = pd.read_csv(data_csv)
      #print(DQ)
      patientids, data = preprocessing(DQ)
      print(type(data))

     # Convert JSON to numpy array
     # predict_request = [data['FIRSTNAME'], data['LASTNAME'], data['GENDERCODE'], data['DATEOFBIRTH'], data['ETHNICITYCODE'], data['RACECODE'], data['MARITALSTATUS']]
      predict_request = np.array(data)
      #predict_request.astype(float)
      print(predict_request)
     # # Predict using the random forest model
      y = xgb_model.predict(predict_request)
      y = np.array(y).reshape((y.shape[0],1))
      patientids = np.array(patientids).reshape((patientids.shape[0],1))
      print(y)
      print(patientids.shape)
      y = pd.DataFrame(y)
      patientids = pd.DataFrame(patientids)
     # Return prediction
      #output = y
      #d = {'col1': PATIENTID , 'col2': PREDICTIONS}
      #result = pd.DataFrame(data=d, index = index)
      results = pd.concat([patientids.reset_index(drop = True), y], axis=1)
      results.columns = ['Patient_id', 'Predictions']
      #results = pd.DataFrame.to_json(results)
      #print(result)
      return render_template("score.html", score=results.to_html())

if __name__ == '__main__':
     app.run(port = 9000, debug = True)