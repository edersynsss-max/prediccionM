import json

# Leer resultados
with open("resultados_simulados.json", "r", encoding="utf-8") as archivo:
    partidos = json.load(archivo)

tabla = {}

for partido in partidos:

    local = partido["local"]
    visitante = partido["visitante"]

    # Ignorar partidos sin equipos definidos
    if local is None or visitante is None:
        continue

    gl = partido["goles_local"]
    gv = partido["goles_visitante"]

    if local not in tabla:
        tabla[local] = {
            "PJ": 0,
            "PG": 0,
            "PE": 0,
            "PP": 0,
            "GF": 0,
            "GC": 0,
            "PTS": 0
        }

    if visitante not in tabla:
        tabla[visitante] = {
            "PJ": 0,
            "PG": 0,
            "PE": 0,
            "PP": 0,
            "GF": 0,
            "GC": 0,
            "PTS": 0
        }

    # Partidos jugados
    tabla[local]["PJ"] += 1
    tabla[visitante]["PJ"] += 1

    # Goles
    tabla[local]["GF"] += gl
    tabla[local]["GC"] += gv

    tabla[visitante]["GF"] += gv
    tabla[visitante]["GC"] += gl

    # Resultado
    if gl > gv:

        tabla[local]["PG"] += 1
        tabla[visitante]["PP"] += 1

        tabla[local]["PTS"] += 3

    elif gv > gl:

        tabla[visitante]["PG"] += 1
        tabla[local]["PP"] += 1

        tabla[visitante]["PTS"] += 3

    else:

        tabla[local]["PE"] += 1
        tabla[visitante]["PE"] += 1

        tabla[local]["PTS"] += 1
        tabla[visitante]["PTS"] += 1


# Ordenar clasificación
clasificacion = sorted(
    tabla.items(),
    key=lambda x: (
        x[1]["PTS"],
        x[1]["GF"] - x[1]["GC"],
        x[1]["GF"]
    ),
    reverse=True
)

print("\n" + "=" * 75)
print("TABLA GENERAL PROYECTADA DEL MUNDIAL 2026")
print("=" * 75)

print(
    f"{'POS':<5}"
    f"{'EQUIPO':<22}"
    f"{'PTS':<6}"
    f"{'PJ':<6}"
    f"{'PG':<6}"
    f"{'PE':<6}"
    f"{'PP':<6}"
    f"{'GF':<6}"
    f"{'GC':<6}"
    f"{'DG':<6}"
)

print("-" * 75)

for pos, (equipo, datos) in enumerate(clasificacion, start=1):

    dg = datos["GF"] - datos["GC"]

    print(
        f"{pos:<5}"
        f"{str(equipo):<22}"
        f"{datos['PTS']:<6}"
        f"{datos['PJ']:<6}"
        f"{datos['PG']:<6}"
        f"{datos['PE']:<6}"
        f"{datos['PP']:<6}"
        f"{datos['GF']:<6}"
        f"{datos['GC']:<6}"
        f"{dg:<6}"
    )