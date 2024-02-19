import json

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_datos(archivo, datos):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)

def registrar_notas_camper():
    campers = cargar_datos('campers.json')
    camper_id = input("Ingrese el ID del camper para registrar notas: ")
    for camper in campers:
        if camper["ID"] == camper_id:
            teoria = float(input("Nota teórica: "))
            practica = float(input("Nota práctica: "))
            camper["nota_teoria"] = teoria
            camper["nota_practica"] = practica
            if (teoria + practica) / 2 >= 60:
                camper["estado"] = "Aprobado"
            guardar_datos('campers.json', campers)
            print("Notas registradas exitosamente.")
            return
    print("Camper no encontrado.")

def asignar_camper_ruta_aprobada():
    campers = cargar_datos('campers.json')
    for camper in campers:
        if camper["estado"] == "Aprobado":
            print(f"Camper ID: {camper['ID']} - Nombre: {camper['nombres']} {camper['apellidos']}")
            print("Asignar a ruta:")
            # Lógica para asignar a una ruta
            print("Camper asignado a ruta exitosamente.")

def evaluar_rendimiento_campers():
    campers = cargar_datos('campers.json')
    for camper in campers:
        if (camper["nota_teoria"] + camper["nota_practica"]) / 2 < 60:
            print(f"Camper ID: {camper['ID']} - Nombre: {camper['nombres']} {camper['apellidos']}")
            print("Bajo rendimiento")
            print("Se requiere atención")

def contar_aprobados_perdidos_modulos():
    rutas = cargar_datos('rutas.json')
    for ruta in rutas:
        aprobados = 0
        perdidos = 0
        for modulo in ruta["modulos"]:
            for camper_id, notas in modulo["notas"].items():
                promedio = sum(notas.values()) / len(notas)
                if promedio >= 60:
                    aprobados += 1
                else:
                    perdidos += 1
        print(f"Ruta: {ruta['nombre']}")
        print(f"Aprobados: {aprobados}")
        print(f"Perdidos: {perdidos}")

def asignar_camper_ruta(camper_id, ruta_nombre):
    campers = cargar_datos('campers.json')
    rutas = cargar_datos('rutas.json')
    for camper in campers:
        if camper["ID"] == camper_id and camper["estado"] == "Aprobado":
            for ruta in rutas:
                if ruta["nombre"] == ruta_nombre:
                    if len(ruta["campers"]) < 33:
                        camper["ruta_asignada"] = ruta_nombre
                        guardar_datos('campers.json', campers)
                        ruta["campers"].append(camper_id)
                        guardar_datos('rutas.json', rutas)
                        print(f"Camper ID: {camper_id} asignado a la ruta {ruta_nombre} exitosamente.")
                        return
                    else:
                        print(f"No hay cupo disponible en la ruta {ruta_nombre}.")
                        return
            print(f"No se encontró la ruta {ruta_nombre}.")
            return
    print(f"No se encontró al camper con ID {camper_id} o no está aprobado para asignarle una ruta.")