import requests
import json

TOKEN = "aa3d18168fc6408abf4a32a480f2f1cd"

headers = {
    "X-Auth-Token": TOKEN
}

response = requests.get(
    "https://api.football-data.org/v4/competitions/2000/standings",
    headers=headers
)

datos = response.json()

with open("standings.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)

print("Archivo standings.json creado")