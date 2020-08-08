import json
import requests




response = requests.get("http://yerkee.com/api/fortune")
print(response.status_code)