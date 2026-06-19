import json
import random

random.seed(2026)

# Cargar ranking
with open("ranking_fifa.json", "r", encoding="utf-8") as archivo:
    ranking = json.load(archivo)

# Cargar partidos
with open("partidos_mundial.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)


def fuerza_equipo(nombre):
    if nombre in ranking:
        return 100 - ranking[nombre]
    return 50


def simular(local, visitante):

    fuerza_local = fuerza_equipo(local)
    fuerza_visitante = fuerza_equipo(visitante)

    diferencia = fuerza_local - fuerza_visitante

    if diferencia > 25:
        return random.randint(2, 4), random.randint(0, 1)

    elif diferencia > 10:
        return random.randint(1, 3), random.randint(0, 2)

    elif diferencia < -25:
        return random.randint(0, 1), random.randint(2, 4)

    elif diferencia < -10:
        return random.randint(0, 2), random.randint(1, 3)

    else:
        return random.randint(0, 2), random.randint(0, 2)


resultados = []

for partido in datos["matches"]:

    local = partido["homeTeam"]["name"]
    visitante = partido["awayTeam"]["name"]

    estado = partido["status"]

    # Resultado real
    if estado == "FINISHED":

        gl = partido["score"]["fullTime"]["home"]
        gv = partido["score"]["fullTime"]["away"]

        resultados.append({
            "local": local,
            "visitante": visitante,
            "goles_local": gl,
            "goles_visitante": gv,
            "real": True
        })

    # Resultado simulado
    else:

        gl, gv = simular(local, visitante)

        resultados.append({
            "local": local,
            "visitante": visitante,
            "goles_local": gl,
            "goles_visitante": gv,
            "real": False
        })


with open("resultados_simulados.json", "w", encoding="utf-8") as archivo:
    json.dump(resultados, archivo, indent=4, ensure_ascii=False)

print("Archivo resultados_simulados.json creado")