from arboles import *
from clienteRegistro import *
def salida ():
    return "salida"
def menu():
    
    menu = """"
            ----------------------------------------------------BIENVENIDO---------------------------------------------------
            Escoge la opción de tu preferencia:
            1. Registrar un cliente 
            2. Buscar y mostrar un cliente
            3. Modificar información de un cliente
            4. Recomendar destinos 
            5. Crear ruta
            6. Utilizar ruta previa  
            7. Salir       
            """
    
    optionsDirectory = {
        1: registrarCliente,
        2: buscar_MostrarCliente,
        3: modificarCliente,
        4: ejecucion_arbol,
        #5: ,
        #6: ,
        7: salida
    }

    while True: 
        print(menu)

        try:
            option = int(input("Ingrese la opción a seleccionar: "))

        except BaseException:
            print("Tienes que ingresar un valor correcto")
            continue

        if option not in optionsDirectory.values():
            break

    selection = optionsDirectory.get(option)

    if selection is None:
        print("Opcion no valida")
        return 
    
    return selection()

def main():
    while True:

        menu()
        if menu() == "salida":
            break
        
main()