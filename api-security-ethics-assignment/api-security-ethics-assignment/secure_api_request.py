import os
import requests

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API key not found in environment variables.")
    exit()

url = "https://api.example.com/data"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Success! JSON response:")
        print(response.json())

    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")

    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
