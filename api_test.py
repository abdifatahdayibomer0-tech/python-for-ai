# This is a test file for API testing

# Get request

import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(URL)
data = response.json()
print("API response received:")
print(data)

if response.status_code == 200:
    print("\nSuccess! status code: 200")

# Post request

data = {"title": "AI Developer", "body": "learning HTTP Methods", "userId": 1}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

print(response.status_code)
print(response.json())
