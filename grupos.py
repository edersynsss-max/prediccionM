import requests

API_KEY = "e98534dc5674df3fab5cc3f4e342cc94"

url = "https://v3.football.api-sports.io/standings?league=1&season=2026"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(url, headers=headers)

print("Código:", response.status_code)

datos = response.json()

print(datos)