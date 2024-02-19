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

def registrar_camper():
    camper = {}
    print("Registro de nuevo camper:")
    camper["ID"] = input("ID del camper: ")
    camper["nombres"] = input("Nombres: ")
    camper["apellidos"] = input("Apellidos: ")
    camper["direccion"] = input("Dirección: ")
    camper["acudiente"] = input("Acudiente: ")
    camper["telefono_celular"] = input("Teléfono celular: ")
    camper["telefono_fijo"] = input("Teléfono fijo: ")
    camper["estado"] = "En proceso de ingreso"
    camper["riesgo"] = "Bajo" if int(camper["ID"]) % 2 == 0 else "Alto"  # Si el ID es par, riesgo bajo
    campers = cargar_datos('campers.json')
    campers.append(camper)
    guardar_datos('campers.json', campers)
    print("Camper registrado exitosamente.")