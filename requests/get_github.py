import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
# This code sends a GET request to the GitHub API and prints the status code and response data.