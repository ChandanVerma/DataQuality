import json, requests

url = 'http://localhost:9000/predict_api'
data = json.dumps({'FIRSTNAME' : 1.5,
		'LASTNAME' : 1.5 , 
		'GENDERCODE' : 1  , 
		'DATEOFBIRTH' : 1.5 , 
		'ETHNICITYCODE' : 2.5 , 
		'RACECODE' : 2.5, 
		'MARITALSTATUS' : 1 })
		
r = requests.post(url, data)

print(r.json())