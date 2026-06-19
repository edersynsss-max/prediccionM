import requests

API_KEY = "e98534dc5674df3fab5cc3f4e342cc94"

url = "https://v3.football.api-sports.io/leagues"

headers = {
    "x-apisports-key": API_KEY
}

response = requests.get(url, headers=headers)

datos = response.json()

for liga in datos["response"]:

    if liga["league"]["name"] == "World Cup":

        print("ID:", liga["league"]["id"])
        print("Nombre:", liga["league"]["name"])

        print("Temporadas disponibles:")

        for temporada in liga["seasons"]:
            print(temporada["year"])