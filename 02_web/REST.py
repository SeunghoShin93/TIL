import requests
import json

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
data={'nickname':'대전1반신승호', 'yourAnswer':'Kubernetes'}
r = requests.post('http://13.125.222.176/quiz/jordan', headers=headers, data=json.dumps(data))


print(r.json())