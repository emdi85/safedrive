import requests

def fetch_data():
    response = requests.get('https://api.vegvesenet.no/your_endpoint')
    return response.json()
