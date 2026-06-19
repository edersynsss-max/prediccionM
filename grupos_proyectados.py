import json

# --------------------------
# CARGAR GRUPOS
# --------------------------

with open("standings.json", "r", encoding="utf-8") as archivo:
    standings = json.load(archivo)

grupos = {}

for grupo in standings["standings"]:

    nombre_grupo = grupo["group"]

    grupos[nombre_grupo] = []

    for equipo in grupo["table"]:

        grupos[nombre_grupo].append(
            equipo["team"]["name"]
        )

# --------------------------
# CARGAR RESULTADOS
# --------------------------

with open("resultados_simulados.json", "r", encoding="utf-8") as archivo:
    partidos = json.load(archivo)

# --------------------------
# CALCULAR TABLAS
# --------------------------

for nombre_grupo, equipos in grupos.items():

    tabla = {}

    for equipo in equipos:

        tabla[equipo] = {
            "PTS": 0,
            "PJ": 0,
            "PG": 0,
            "PE": 0,
            "PP": 0,
            "GF": 0,
            "GC": 0
        }

    for partido in partidos:

        local = partido["local"]
        visitante = partido["visitante"]

        if local not in equipos:
            continue

        if visitante not in equipos:
            continue

        gl = partido["goles_local"]
        gv = partido["goles_visitante"]

        tabla[local]["PJ"] += 1
        tabla[visitante]["PJ"] += 1

        tabla[local]["GF"] += gl
        tabla[local]["GC"] += gv

        tabla[visitante]["GF"] += gv
        tabla[visitante]["GC"] += gl

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

    clasificacion = sorted(
        tabla.items(),
        key=lambda x: (
            x[1]["PTS"],
            x[1]["GF"] - x[1]["GC"],
            x[1]["GF"]
        ),
        reverse=True
    )

    print("\n" + "=" * 60)
    print(nombre_grupo.upper())
    print("=" * 60)

    print(
        f"{'POS':<5}"
        f"{'EQUIPO':<22}"
        f"{'PTS':<6}"
        f"{'PJ':<6}"
        f"{'DG':<6}"
    )

    print("-" * 60)

    for pos, (equipo, datos) in enumerate(clasificacion, start=1):

        dg = datos["GF"] - datos["GC"]

        print(
            f"{pos:<5}"
            f"{equipo:<22}"
            f"{datos['PTS']:<6}"
            f"{datos['PJ']:<6}"
            f"{dg:<6}"
        )