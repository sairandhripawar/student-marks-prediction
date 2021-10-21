import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'study_hours':10})

print(r.json())