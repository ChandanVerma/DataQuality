import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pandasql as pdsql

def preprocessing(DQ):
	DQ = DQ[['PATIENTID', 'FIRSTNAME', 'LASTNAME', 'GENDERCODE', 'DATEOFBIRTH', 'ETHNICITYCODE', 'RACECODE', 'MARITALSTATUS']]
	DQ.replace('null', 1.5,inplace=True)
	DQ.replace('NULL', 1.5,inplace=True)
	#print('------------- Values after replacing ------------------')
	#print(DQ.head())
	
	# print(DQ.GENDERCODE.value_counts())
	# pysql = lambda q: pdsql.sqldf(q, globals())
	# str1 = "select distinct PATIENTID as Distinct_Patients from DQ;"
	# df1 = pysql(str1)
	# print(df1)
	
	#print('-------------------------------------------------------')
	DQ.ix[DQ.FIRSTNAME != 1.5, 'FIRSTNAME'] = 0
	#print(DQ.FIRSTNAME.value_counts())
	
	#print('-------------------------------------------------------')
	DQ.ix[DQ.LASTNAME != 1.5, 'LASTNAME'] = 0
	#print(DQ.LASTNAME.value_counts())
	
	#print('-------------------------------------------------------')
	DQ.GENDERCODE = np.where(((DQ.GENDERCODE == 'M') | (DQ.GENDERCODE == 'F')),DQ.GENDERCODE,2.5)
	DQ.ix[DQ.GENDERCODE == 'M', 'GENDERCODE'] = 0
	DQ.ix[DQ.GENDERCODE == 'F', 'GENDERCODE'] = 1
	#print(DQ.GENDERCODE.value_counts())
	
	#print('-------------------------------------------------------')
	DQ.DATEOFBIRTH = np.where((DQ.DATEOFBIRTH == 1.5),DQ.DATEOFBIRTH,0)
	#print(DQ.DATEOFBIRTH.value_counts())
	
	#print('-------------------------------------------------------')
	DQ.ETHNICITYCODE = np.where((DQ.ETHNICITYCODE != '2186-5'),2.5,DQ.ETHNICITYCODE)
	DQ.ix[DQ.ETHNICITYCODE == '2186-5', 'ETHNICITYCODE'] = 1
	#print(DQ.ETHNICITYCODE.value_counts())
	
	#print('-------------------------------------------------------')
	DQ.ix[DQ.RACECODE == '2106-3', 'RACECODE'] = 3
	DQ.ix[DQ.RACECODE == '2054-5', 'RACECODE'] = 5
	DQ.ix[DQ.RACECODE == '2076-8', 'RACECODE'] = 8
	DQ.ix[DQ.RACECODE == '2131-1', 'RACECODE'] = 1
	DQ.ix[DQ.RACECODE == '2028-9', 'RACECODE'] = 9
	DQ.RACECODE = np.where(((DQ.RACECODE == 3) | (DQ.RACECODE == 5) | (DQ.RACECODE == 8) | (DQ.RACECODE == 1) | (DQ.RACECODE == 9)),DQ.RACECODE,2.5)
	#print(DQ.RACECODE.value_counts())
	
	#print('-------------------------------------------------------')
	DQ.ix[DQ.MARITALSTATUS == 'M', 'MARITALSTATUS'] = 1
	DQ.ix[DQ.MARITALSTATUS == 'S', 'MARITALSTATUS'] = 2
	DQ.ix[DQ.MARITALSTATUS == 'X', 'MARITALSTATUS'] = 2.5
	DQ.ix[DQ.MARITALSTATUS == 'W', 'MARITALSTATUS'] = 3
	#print(DQ.MARITALSTATUS.value_counts())
	patientids = DQ['PATIENTID']
	DQ = DQ[['FIRSTNAME', 'LASTNAME', 'GENDERCODE', 'DATEOFBIRTH', 'ETHNICITYCODE', 'RACECODE', 'MARITALSTATUS']]
	return patientids , DQ

