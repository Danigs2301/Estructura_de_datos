from tda_lista import *
import time

class Cliente(object): #clase del cliente
    def __init__(self, nombre, id, numero_pasaporte, idiomas, viaja_solo, acompañantes=None):
        self.nombre = nombre
        self.id = id
        self.numero_pasaporte = numero_pasaporte
        self.idiomas = idiomas
        self.viaja_solo = viaja_solo
        self.acompañantes = [] if acompañantes is None else acompañantes

def buscar(lista, buscado): #buscar a los cliente por su identificacion
    aux = lista.inicio
    while aux is not None:
        if aux.info["Cédula"] == buscado:
            return aux
        aux = aux.sig
    return None

lista = Lista()
while True:
    print("\nMenú de opciones:")
    print("1. Registrar un cliente")
    print("2. Buscar y mostrar un cliente")
    print("3. Modificar información de un cliente")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        datos = {} #lista para almacenar los datos del cliente e insertarlos en la Lista()
        nombre = input("Ingrese el nombre completo del cliente: ").capitalize() #.capitalize para poner la primera letra en mayuscula
        cedula = input("Ingrese el número de identificación: ")
        numero_pasaporte = input("Ingrese el número de pasaporte: ")
        idiomas = input("Idiomas hablados (separados por comas): ").split(', ')
        viaja_solo = input("¿Viaja solo? (Si/No): ").lower() == 'si'
        acompañantes = []

        if not viaja_solo:
            num_acompañantes = int(input("Número de personas que viajan con el cliente: "))
            for i in range(num_acompañantes):
                acompañante_nombre = input(f"Ingrese el nombre del acompañante {i + 1}: ").capitalize()
                acompañantes.append(acompañante_nombre)

        cliente = Cliente(nombre, cedula, numero_pasaporte, idiomas, viaja_solo, acompañantes)

        datos["Nombre"] = cliente.nombre
        datos["Cédula"] = cliente.id
        datos["Número de Pasaporte"] = cliente.numero_pasaporte
        datos["Idiomas Hablados"] = cliente.idiomas
        datos["Viaja Solo"] = cliente.viaja_solo
        datos["Acompañantes"] = cliente.acompañantes

        insertar(lista, datos)
        print("¡Registro exitoso! El cliente ha sido registrado con éxito.")
        time.sleep(2) #demora el codigo para visualizar los mensajes
    elif opcion == "2":
        cedula = input("Ingrese el número de identificación del cliente: ")
        clienteBuscado = buscar(lista, cedula)
        if clienteBuscado: #si el cliente existe se muestran los datos
            cliente = clienteBuscado.info
            print(f"Nombre: {cliente['Nombre']}")
            print(f"Cédula: {cliente['Cédula']}")
            print(f"Número de Pasaporte: {cliente['Número de Pasaporte']}")
            print(f"Idiomas Hablados: {', '.join(cliente['Idiomas Hablados'])}")
            print(f"Viaja Solo: {'Sí' if cliente['Viaja Solo'] else 'No'}") #operador ternario
                                #valor_verdadero if condicion else valor_falso, devuelve true o false dependiendo el valor tomado

            if not cliente['Viaja Solo']:
                print("Acompañantes:")
                for i, acompañante in enumerate(cliente['Acompañantes'], 1): #enumertae recibe objetos iterables para enumerar
                    print(f"{i}. {acompañante}")
        else:
            print("El número de identificación no coincide.")
            time.sleep(2)

    elif opcion == "3":
        print("Modificar y actualizar información del cliente")

        id_modificar = input("Ingrese el número de identificación del cliente que desea modificar: ")
        cliente_encontrado = buscar(lista, id_modificar)

        if cliente_encontrado:
            cliente = cliente_encontrado.info #se accede a la informacion del cliente
            print("Cliente encontrado. Seleccione qué desea modificar:")
            print("1. Nombre")
            print("2. Número de Pasaporte")
            print("3. Idiomas Hablados")
            print("4. ¿Viaja Solo?")
            print("5. Volver al Menú Principal")

            opc = input("Seleccione una opción: ")

            while opc != "5": # se repite el menu hasta que el cliente decida regresar al menu principal
                if opc == "1":
                    nuevo_nombre = input("Nuevo nombre: ").capitalize()
                    cliente['Nombre'] = nuevo_nombre
                    print("¡Cambios realizados con éxito!")
                    time.sleep(2)

                elif opc == "2":
                    nuevo_numero_pasaporte = input("Nuevo número de pasaporte: ")
                    cliente['Número de Pasaporte'] = nuevo_numero_pasaporte
                    print("¡Cambios realizados con éxito!")
                    time.sleep(2)

                elif opc == "3":
                    nuevos_idiomas = input("Nuevos idiomas hablados (separados por comas): ").split(', ')
                    cliente['Idiomas Hablados'] = nuevos_idiomas
                    print("¡Cambios realizados con éxito!")
                    time.sleep(2)

                elif opc == "4":
                    nuevo_viaja_solo = input("¿Viaja solo? (Si/No): ").lower() == 'si'
                    cliente['Viaja Solo'] = nuevo_viaja_solo

                    if not nuevo_viaja_solo:
                        num_acompañantes = int(input("Número de personas que viajan con el cliente: "))
                        acompañantes = []
                        for i in range(num_acompañantes):
                            acompañante_nombre = input(f"Ingrese el nombre del acompañante {i + 1}: ").capitalize()
                            acompañantes.append(acompañante_nombre)
                        cliente['Acompañantes'] = acompañantes

                    print("¡Cambios realizados con éxito!")
                    time.sleep(2)

                else:
                    print("Opción no válida")

                print("\nSeleccione qué desea modificar:")
                print("1. Nombre")
                print("2. Número de Pasaporte")
                print("3. Idiomas Hablados")
                print("4. ¿Viaja Solo?")
                print("5. Volver al Menú Principal")

                opc = input("Seleccione una opción: ")

            print("Cargando menu principal")
            time.sleep(2)
        else:
            print("El número de identificación no coincide")
            time.sleep(2)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        time.sleep(2)