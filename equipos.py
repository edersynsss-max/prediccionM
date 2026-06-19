import requests

TOKEN = "aa3d18168fc6408abf4a32a480f2f1cd"

headers = {
    "X-Auth-Token": TOKEN
}

response = requests.get(
    "https://api.football-data.org/v4/competitions/2000/teams",
    headers=headers
)

datos = response.json()

print("Código:", response.status_code)

for equipo in datos["teams"]:
    print(equipo["name"])