import requests
from pprint import pprint

def client():
    credentials = {
        "username": "rest_test_user",
        "email": "test@test.co",
        "password1": "testuser321..",
        "password2": "testuser321..",
    }

    response = requests.post(
        url = "http://127.0.0.1:8000/api/rest-auth/registration/",
        data = credentials        
    )

    print(f"Response Status Code: {response.status_code}")
    response_data = response.json()
    pprint(response_data)

if __name__ == "__main__":
    client()