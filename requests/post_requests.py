import requests

url = 'https://httpbin.org/post'
data = {'username': 'devopsuser', 'role': 'admin'}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
# This code sends a POST request to httpbin.org with JSON data and prints the status code and response data.