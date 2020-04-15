import requests

r = requests.get('http://localhost:8080/api/v1/test')
print(r.status_code)