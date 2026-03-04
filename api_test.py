# This is a test file for API testing

import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(URL)
data = response.json()
print("API response received:")
print(data)

if response.status_code == 200:
    print("\nSuccess! status code: 200")
