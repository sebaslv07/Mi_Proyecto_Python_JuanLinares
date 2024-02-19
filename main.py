from camper import *
from trainer import *
from coordinador import *

def menu_principal():
    print("\nBienvenido al sistema de CampusLands:")
    print("1. Menú Camper")
    print("2. Menú Trainer")
    print("3. Menú Coordinador")
    print("4. Salir")

def menu_camper():
    print("\nMenú Camper:")
    print("1. Registrar")
    print("2. Salir")

def menu_trainer():
    print("\nMenú Trainer:")
    print("1. Listar clases")
    print("2. Asignar camper a ruta")
    print("3. Salir")

def menu_coordinador():
    print("\nMenú Coordinador:")
    print("1. Registrar notas camper")
    print("2. Asignar camper a ruta aprobada")
    print("3. Evaluar rendimiento campers")
    print("4. Contar aprobados y perdidos por módulo")
    print("5. Salir")

def main():
    while True:
        menu_principal()
        opcion_principal = input("Ingrese la opción deseada: ")

        if opcion_principal == "1":
            while True:
                menu_camper()
                opcion_camper = input("Ingrese la opción deseada: ")
                if opcion_camper == "1":
                    registrar_camper()
                elif opcion_camper == "2":
                    break
                else:
                    print("Opción inválida.")

        elif opcion_principal == "2":
            while True:
                menu_trainer()
                opcion_trainer = input("Ingrese la opción deseada: ")
                if opcion_trainer == "1":
                    trainer_id = input("Ingrese el ID del Trainer: ")
                    listar_clases_trainer(trainer_id)
                elif opcion_trainer == "2":
                    camper_id = input("Ingrese el ID del Camper: ")
                    ruta_nombre = input("Ingrese el nombre de la ruta: ")
                    asignar_camper_ruta(camper_id, ruta_nombre)
                elif opcion_trainer == "3":
                    break
                else:
                    print("Opción inválida.")

        elif opcion_principal == "3":
            while True:
                menu_coordinador()
                opcion_coordinador = input("Ingrese la opción deseada: ")
                if opcion_coordinador == "1":
                    registrar_notas_camper()
                elif opcion_coordinador == "2":
                    asignar_camper_ruta_aprobada()
                elif opcion_coordinador == "3":
                    evaluar_rendimiento_campers()
                elif opcion_coordinador == "4":
                    contar_aprobados_perdidos_modulos()
                elif opcion_coordinador == "5":
                    break
                else:
                    print("Opción inválida.")

        elif opcion_principal == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
