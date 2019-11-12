import requests

url = 'http://reqres.in/api/users/23'
response = requests.get(url)
print(response.status_code)
print()
print(response.headers)
print()
print(response.json())
