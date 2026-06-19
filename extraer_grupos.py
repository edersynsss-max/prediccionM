import json

with open("standings.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

grupos = {}

for grupo in datos["standings"]:

    nombre_grupo = grupo["group"]

    equipos = []

    for equipo in grupo["table"]:
        equipos.append(equipo["team"]["name"])

    grupos[nombre_grupo] = equipos

for nombre, equipos in grupos.items():

    print("\n" + nombre)

    for equipo in equipos:
        print("-", equipo)
        