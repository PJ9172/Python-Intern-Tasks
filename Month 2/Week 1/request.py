import requests

# Requesting to github api
response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json())