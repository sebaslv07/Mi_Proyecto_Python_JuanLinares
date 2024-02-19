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

def listar_clases_trainer(trainer_id):
    trainers = cargar_datos('trainers.json')
    for trainer in trainers:
        if trainer["ID"] == trainer_id:
            print(f"Clases del trainer {trainer['nombre']}:")
            for clase in trainer["clases"]:
                print(clase)

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
