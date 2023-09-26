import requests

api_url = "http://localhost:8000/temperature/city"

try:
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print("API Response")
        print(data)
    else:
        print(f"Failed to Retrieve Data")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e} ")