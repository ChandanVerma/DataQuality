from sklearn.pipeline import make_pipeline
from xgboost import XGBClassifier
from Codefile import *
import sklearn
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import warnings
import pickle
from __future__ import print_function
import os
from sklearn.externals import joblib
warnings.filterwarnings("ignore")
if __name__ == "__main__":
	X = DQ[['PATIENTID', 'FIRSTNAME', 'LASTNAME', 'GENDERCODE', 'DATEOFBIRTH', 'ETHNICITYCODE', 'RACECODE', 'MARITALSTATUS']]
	print('------------------- X Head ------------------------------------')
	print(X.head())
	print('---------------  --------------------------')
	y = DQ[['DQ_STATUS']]
	print('------------------- Y head ------------------------------------')
	print(y.head())
	print('-------------------------------------------------------')
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
	X_train_ids = X_train[['PATIENTID']]
	X_test_ids = X_test[['PATIENTID']]
	X_train = X_train[['FIRSTNAME', 'LASTNAME', 'GENDERCODE', 'DATEOFBIRTH', 'ETHNICITYCODE', 'RACECODE', 'MARITALSTATUS']]
	X_test = X_test[['FIRSTNAME', 'LASTNAME', 'GENDERCODE', 'DATEOFBIRTH', 'ETHNICITYCODE', 'RACECODE', 'MARITALSTATUS']]
	X_train=np.array(X_train)
	X_test=np.array(X_test) 
	X_train = X_train.astype(float) 
	X_test = X_test.astype(float)
	
	y_train=np.array(y_train)
	y_test=np.array(y_test) 
	y_train = y_train.astype(float) 
	y_test = y_test.astype(float)
	
	# print('--------------------- X_train.head ----------------------------------')
	# print(X_train.head())
	# print('---------------------- X_test.head ---------------------------------')
	# print(X_test.head())
	# print('----------------------- Y_train.head --------------------------------')
	# print(y_train.head())
	# print('------------------------ Y_test.head -------------------------------')
	# print(y_test.head())
	# print(type(y_test.head))
	# print('-------------------------------------------------------')
	
	
	model = XGBClassifier()
	model.fit(X_train, y_train)
	
	print(model)
	filename = 'xgb_model.pkl'
	joblib.dump(model, filename)
	print("Successfully Built and Picked into models folder")
	#pickle.dump(model, open(filename, 'wb'))
	# # make predictions for test data
	# y_pred = xgb_model.predict(X_test)
	# predictions = [round(value) for value in y_pred]
	
	# accuracy = accuracy_score(y_test, predictions)
	# print("Accuracy: %.2f%%" % (accuracy * 100.0))