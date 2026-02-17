import requests
from pprint import pprint

def client():
    token = "Token 4e2ffb8c112626bdd5eed31c2438d9b8ac8a628e"

    headers = {
        "Authorization": token,
    }
    response = requests.get(
        url = "http://127.0.0.1:8000/api/kullanici-profilleri",
        headers = headers,
    )

    print(f"Status Code: {response.status_code}")
    response_data = response.json()
    pprint(response_data)

if __name__ == "__main__":
    client()