from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def inicio():

    with open("resultados_simulados.json", "r", encoding="utf-8") as archivo:
        partidos = json.load(archivo)

    grupos = {
        "Group A": ["Mexico", "South Korea", "Czechia", "South Africa"],
        "Group B": ["Switzerland", "Canada", "Qatar", "Bosnia-Herzegovina"],
        "Group C": ["Scotland", "Morocco", "Brazil", "Haiti"],
        "Group D": ["United States", "Australia", "Turkey", "Paraguay"],
        "Group E": ["Germany", "Ivory Coast", "Ecuador", "Curaçao"],
        "Group F": ["Sweden", "Japan", "Netherlands", "Tunisia"],
        "Group G": ["New Zealand", "Iran", "Belgium", "Egypt"],
        "Group H": ["Uruguay", "Saudi Arabia", "Spain", "Cape Verde Islands"],
        "Group I": ["France", "Norway", "Iraq", "Senegal"],
        "Group J": ["Algeria", "Argentina", "Jordan", "Austria"],
        "Group K": ["Congo DR", "Colombia", "Portugal", "Uzbekistan"],
        "Group L": ["England", "Ghana", "Croatia", "Panama"]
    }

    tablas = {}

    for nombre_grupo, equipos in grupos.items():

        tabla = {}

        for equipo in equipos:
            tabla[equipo] = {
                "nombre": equipo,
                "pts": 0,
                "pj": 0,
                "gf": 0,
                "gc": 0,
                "dg": 0
            }

        for partido in partidos:

            local = partido["local"]
            visitante = partido["visitante"]

            if local not in equipos or visitante not in equipos:
                continue

            gl = partido["goles_local"]
            gv = partido["goles_visitante"]

            tabla[local]["pj"] += 1
            tabla[visitante]["pj"] += 1

            tabla[local]["gf"] += gl
            tabla[local]["gc"] += gv

            tabla[visitante]["gf"] += gv
            tabla[visitante]["gc"] += gl

            if gl > gv:
                tabla[local]["pts"] += 3

            elif gv > gl:
                tabla[visitante]["pts"] += 3

            else:
                tabla[local]["pts"] += 1
                tabla[visitante]["pts"] += 1

        for equipo in tabla.values():
            equipo["dg"] = equipo["gf"] - equipo["gc"]

        clasificacion = sorted(
            tabla.values(),
            key=lambda x: (
                x["pts"],
                x["dg"],
                x["gf"]
            ),
            reverse=True
        )

        tablas[nombre_grupo] = clasificacion

    return render_template(
        "index.html",
        grupos=tablas
    )

if __name__ == "__main__":
    app.run(debug=True)