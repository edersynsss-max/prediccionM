import requests

API_KEY = "e98534dc5674df3fab5cc3f4e342cc94"

url = "https://v3.football.api-sports.io/timezone"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(url, headers=headers)

print("Código de respuesta:", response.status_code)
print(response.json())