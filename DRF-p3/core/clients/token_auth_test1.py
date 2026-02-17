import requests
from pprint import pprint

def client():


    #{'key': '4e2ffb8c112626bdd5eed31c2438d9b8ac8a628e'}

    credentials = {
        'username' : 'testuser11',
        'password' : 'testing321..',
    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/login/',
        data= credentials
    )

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()