import json
import random
random.seed(2026)


# Cargar ranking FIFA
with open("ranking_fifa.json", "r", encoding="utf-8") as archivo:
    ranking = json.load(archivo)


def obtener_fuerza(equipo):
    if equipo in ranking:
        return 100 - ranking[equipo]

    return 50


def simular_partido(local, visitante):

    fuerza_local = obtener_fuerza(local)
    fuerza_visitante = obtener_fuerza(visitante)

    diferencia = fuerza_local - fuerza_visitante

    # Equipos muy parejos
    if abs(diferencia) <= 5:
        goles_local = random.randint(0, 2)
        goles_visitante = random.randint(0, 2)

    # Favorito moderado
    elif diferencia > 5:

        goles_local = random.randint(1, 4)

        if diferencia > 25:
            goles_visitante = random.randint(0, 1)
        else:
            goles_visitante = random.randint(0, 2)

    else:

        goles_visitante = random.randint(1, 4)

        if diferencia < -25:
            goles_local = random.randint(0, 1)
        else:
            goles_local = random.randint(0, 2)

    return goles_local, goles_visitante


# Prueba
local = "Mexico"
visitante = "South Africa"

goles_local, goles_visitante = simular_partido(local, visitante)

print(f"{local} {goles_local} - {goles_visitante} {visitante}")