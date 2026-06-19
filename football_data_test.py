import requests

TOKEN = "aa3d18168fc6408abf4a32a480f2f1cd"

headers = {
    "X-Auth-Token": TOKEN
}

response = requests.get(
    "https://api.football-data.org/v4/competitions",
    headers=headers
)

print("Código:", response.status_code)
print(response.json())