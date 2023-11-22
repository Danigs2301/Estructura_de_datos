import networkx as nx
import matplotlib.pyplot as plt
import os

from TDAGrafos import *

def reconstruir_camino(warshall, inicio, fin):
    camino = []

    # Obtener los índices de inicio y fin.
    indice_inicio = g.vertices.index(inicio)
    indice_fin = g.vertices.index(fin)

    # Verificar si hay un camino entre los vértices.
    if warshall[indice_inicio][indice_fin] is None:
        return camino  # Devolver lista vacía en lugar de None

    # Reconstruir el camino.
    while inicio != fin:
        siguiente_vertice = warshall[g.vertices.index(inicio)][g.vertices.index(fin)]

        # Verificar si hay un ciclo infinito o un camino no conectado.
        if siguiente_vertice == inicio or siguiente_vertice is None:
            return camino  # Devolver lista vacía en lugar de None

        camino.append(siguiente_vertice)
        inicio = siguiente_vertice

    camino.append(fin)

    return camino


if __name__ == "__main__":
    # FUNCIÓN PARA MANDAR LOS ARGUMENTOS A LA LIBRERIÍA PARA  GRAFICAR
    def grafica(G, u, v, w=1, di=True):
        G.add_edge(u, v, weight=w)

        if not di:
            G.add_edge(v, u, weight=w)


    # CREA GRAFO NORMAL
    g = Grafo()

    # CREA GRAFO DIRIGIDO PARA GRAFICAR - si se desea un grafo no dirigo se quita el "Di" y solo se deja "Graph()"
    #G = nx.DiGraph()
    G = nx.Graph()

    # SE AÑADEN LOS VERTICES AL GRAFO

    g.agregar_vertices("Ginebra (CERN)")
    g.agregar_vertices("California (Silicon)")
    g.agregar_vertices("Atenas (Acrópolis de Atenas)")
    g.agregar_vertices("Agra (Taj Mahal)")
    g.agregar_vertices("Antofagasta (Atacama)")
    g.agregar_vertices("Cairo (Sahara)")
    g.agregar_vertices("Hawai (Maui)")
    g.agregar_vertices("Queensland (Gold Coast)")
    g.agregar_vertices("Patagonia (Monte Fitz Roy)")
    g.agregar_vertices("California (El Capitan)")
    g.agregar_vertices("Yucatán (Chichen Itzá)")
    g.agregar_vertices("Ma'an (Petra)")
    g.agregar_vertices("Madrid (Museo Nacional del Prado)")
    g.agregar_vertices("París (Louvre Museum)")
    g.agregar_vertices("Gettysburg (Gettysburg National Military Park)")
    g.agregar_vertices("Marathon (Battlefield of Marathon)")
    g.agregar_vertices("Cuzco (Machu Picchu)")
    g.agregar_vertices("Roma (Roma)")
    g.agregar_vertices("Borneo (Borneo Rainforest)")
    g.agregar_vertices("Brasilia (Amazonia)")
    g.agregar_vertices("Cantabria (Cueva de Altamira)")
    g.agregar_vertices("Nuevo México (Cuevas de Carlsbad)")
    g.agregar_vertices("Versalles (Jardines de Versalles)")
    g.agregar_vertices("Brentwood Bay (Butchart Gardens)")
    g.agregar_vertices("Atacama (Valle de la Luna)")
    g.agregar_vertices("Bergen (Fiordos de Noruega)")
    g.agregar_vertices("Marrakech (La Palmeraie Marrakech)")
    g.agregar_vertices("Paradise Island (Atlantis)")
    g.agregar_vertices("Digue (Anse Source d'Argent)")
    g.agregar_vertices("Whitsunday Island (Whitehaven Beach)")
    g.agregar_vertices("Thua Hin (Chiva Som)")
    g.agregar_vertices("Alicante (Sha Wellness Clinic)")
    g.agregar_vertices("Costa Azul (Niza)")
    g.agregar_vertices("Cancún (Quintana Roo)")
    g.agregar_vertices("Grindavik (Blue Lagoon)")
    g.agregar_vertices("Mendoza (Termas de Cacheuta)")
    g.agregar_vertices("Cali (Aeropuerto)")

    # SE AÑADEN LAS ARISTAS AL GRAFO
    g.agregar_arista("Ginebra (CERN)", "California (Silicon)", 8000, False)
    g.agregar_arista("Ginebra (CERN)", "Atenas (Acrópolis de Atenas)", 15000, False)
    g.agregar_arista("Ginebra (CERN)", "Agra (Taj Mahal)", 20000, False)
    g.agregar_arista("Ginebra (CERN)", "Antofagasta (Atacama)", 18000, False)
    g.agregar_arista("Ginebra (CERN)", "Cairo (Sahara)", 25000, False)

    g.agregar_arista("California (Silicon)", "Queensland (Gold Coast)", 12000, False)
    g.agregar_arista("California (Silicon)", "Patagonia (Monte Fitz Roy)", 22000, False)
    g.agregar_arista("California (Silicon)", "Yucatán (Chichen Itzá)", 18000, False)
    g.agregar_arista("California (Silicon)", "Madrid (Museo Nacional del Prado)", 18000, False)
    g.agregar_arista("California (Silicon)", "Roma (Roma)", 25000, False)

    g.agregar_arista("Atenas (Acrópolis de Atenas)", "Borneo (Borneo Rainforest)", 20000, False)
    g.agregar_arista("Atenas (Acrópolis de Atenas)", "Brasilia (Amazonia)", 25000, False)
    g.agregar_arista("Atenas (Acrópolis de Atenas)", "Cantabria (Cueva de Altamira)", 18000, False)
    g.agregar_arista("Atenas (Acrópolis de Atenas)", "Versalles (Jardines de Versalles)", 22000, False)
    g.agregar_arista("Atenas (Acrópolis de Atenas)", "Cancún (Quintana Roo)", 20000, False)

    g.agregar_arista("Agra (Taj Mahal)", "Madrid (Museo Nacional del Prado)", 15000, False)
    g.agregar_arista("Agra (Taj Mahal)", "París (Louvre Museum)", 12000, False)
    g.agregar_arista("Agra (Taj Mahal)", "Gettysburg (Gettysburg National Military Park)", 18000, False)
    g.agregar_arista("Agra (Taj Mahal)", "Marrakech (La Palmeraie Marrakech)", 22000, False)
    g.agregar_arista("Agra (Taj Mahal)", "Digue (Anse Source d'Argent)", 25000, False)

    g.agregar_arista("Antofagasta (Atacama)", "Cairo (Sahara)", 12000, False)
    g.agregar_arista("Antofagasta (Atacama)", "Hawai (Maui)", 18000, False)
    g.agregar_arista("Antofagasta (Atacama)", "Cuzco (Machu Picchu)", 22000, False)
    g.agregar_arista("Antofagasta (Atacama)", "Borneo (Borneo Rainforest)", 15000, False)
    g.agregar_arista("Antofagasta (Atacama)", "Bergen (Fiordos de Noruega)", 20000, False)

    g.agregar_arista("Cairo (Sahara)", "Queensland (Gold Coast)", 25000, False)
    g.agregar_arista("Cairo (Sahara)", "Patagonia (Monte Fitz Roy)", 18000, False)
    g.agregar_arista("Cairo (Sahara)", "California (El Capitan)", 22000, False)
    g.agregar_arista("Cairo (Sahara)", "Brentwood Bay (Butchart Gardens)", 25000, False)
    g.agregar_arista("Cairo (Sahara)", "Marrakech (La Palmeraie Marrakech)", 12000, False)

    g.agregar_arista("Hawai (Maui)", "Marathon (Battlefield of Marathon)", 18000, False)
    g.agregar_arista("Hawai (Maui)", "Cuzco (Machu Picchu)", 22000, False)
    g.agregar_arista("Hawai (Maui)", "Roma (Roma)", 25000, False)
    g.agregar_arista("Hawai (Maui)", "Nuevo México (Cuevas de Carlsbad)", 12000, False)
    g.agregar_arista("Hawai (Maui)", "Whitsunday Island (Whitehaven Beach)", 18000, False)

    g.agregar_arista("Queensland (Gold Coast)", "Paradise Island (Atlantis)", 15000, False)
    g.agregar_arista("Queensland (Gold Coast)", "Digue (Anse Source d'Argent)", 20000, False)
    g.agregar_arista("Queensland (Gold Coast)", "Thua Hin (Chiva Som)", 22000, False)
    g.agregar_arista("Queensland (Gold Coast)", "Alicante (Sha Wellness Clinic)", 25000, False)
    g.agregar_arista("Queensland (Gold Coast)", "Costa Azul (Niza)", 12000, False)

    g.agregar_arista("Patagonia (Monte Fitz Roy)", "Atacama (Valle de la Luna)", 18000, False)
    g.agregar_arista("Patagonia (Monte Fitz Roy)", "Bergen (Fiordos de Noruega)", 22000, False)
    g.agregar_arista("Patagonia (Monte Fitz Roy)", "Marrakech (La Palmeraie Marrakech)", 25000, False)
    g.agregar_arista("Patagonia (Monte Fitz Roy)", "Paradise Island (Atlantis)", 12000, False)
    g.agregar_arista("Patagonia (Monte Fitz Roy)", "Whitsunday Island (Whitehaven Beach)", 18000, False)

    g.agregar_arista("California (El Capitan)", "Cantabria (Cueva de Altamira)", 18000, False)
    g.agregar_arista("California (El Capitan)", "Nuevo México (Cuevas de Carlsbad)", 22000, False)
    g.agregar_arista("California (El Capitan)", "Versalles (Jardines de Versalles)", 25000, False)
    g.agregar_arista("California (El Capitan)", "Brentwood Bay (Butchart Gardens)", 12000, False)
    g.agregar_arista("California (El Capitan)", "Atacama (Valle de la Luna)", 15000, False)

    g.agregar_arista("Yucatán (Chichen Itzá)", "Roma (Roma)", 20000, False)
    g.agregar_arista("Yucatán (Chichen Itzá)", "Borneo (Borneo Rainforest)", 25000, False)
    g.agregar_arista("Yucatán (Chichen Itzá)", "Brasilia (Amazonia)", 12000, False)
    g.agregar_arista("Yucatán (Chichen Itzá)", "Cantabria (Cueva de Altamira)", 18000, False)
    g.agregar_arista("Yucatán (Chichen Itzá)", "Nuevo México (Cuevas de Carlsbad)", 22000, False)

    g.agregar_arista("Ma'an (Petra)", "Brentwood Bay (Butchart Gardens)", 18000, False)
    g.agregar_arista("Ma'an (Petra)", "Atacama (Valle de la Luna)", 22000, False)
    g.agregar_arista("Ma'an (Petra)", "Bergen (Fiordos de Noruega)", 25000, False)
    g.agregar_arista("Ma'an (Petra)", "Marrakech (La Palmeraie Marrakech)", 12000, False)
    g.agregar_arista("Ma'an (Petra)", "Paradise Island (Atlantis)", 15000, False)

    g.agregar_arista("Madrid (Museo Nacional del Prado)", "Digue (Anse Source d'Argent)", 20000, False)
    g.agregar_arista("Madrid (Museo Nacional del Prado)", "Whitsunday Island (Whitehaven Beach)", 22000, False)
    g.agregar_arista("Madrid (Museo Nacional del Prado)", "Thua Hin (Chiva Som)", 25000, False)
    g.agregar_arista("Madrid (Museo Nacional del Prado)", "Alicante (Sha Wellness Clinic)", 12000, False)
    g.agregar_arista("Madrid (Museo Nacional del Prado)", "Costa Azul (Niza)", 18000, False)

    g.agregar_arista("París (Louvre Museum)", "Bergen (Fiordos de Noruega)", 18000, False)
    g.agregar_arista("París (Louvre Museum)", "Marrakech (La Palmeraie Marrakech)", 22000, False)
    g.agregar_arista("París (Louvre Museum)", "Paradise Island (Atlantis)", 25000, False)
    g.agregar_arista("París (Louvre Museum)", "Digue (Anse Source d'Argent)", 12000, False)
    g.agregar_arista("París (Louvre Museum)", "Whitsunday Island (Whitehaven Beach)", 15000, False)

    g.agregar_arista("Gettysburg (Gettysburg National Military Park)", "Alicante (Sha Wellness Clinic)", 20000, False)
    g.agregar_arista("Gettysburg (Gettysburg National Military Park)", "Costa Azul (Niza)", 25000, False)
    g.agregar_arista("Gettysburg (Gettysburg National Military Park)", "Cancún (Quintana Roo)", 12000, False)
    g.agregar_arista("Gettysburg (Gettysburg National Military Park)", "Grindavik (Blue Lagoon)", 18000, False)
    g.agregar_arista("Gettysburg (Gettysburg National Military Park)", "Mendoza (Termas de Cacheuta)", 22000, False)

    g.agregar_arista("Cali (Aeropuerto)", "París (Louvre Museum)", 12000, False)
    g.agregar_arista("Cali (Aeropuerto)", "Cairo (Sahara)", 18000, False)
    g.agregar_arista("Cali (Aeropuerto)", "Hawai (Maui)", 22000, False)
    g.agregar_arista("Cali (Aeropuerto)", "Versalles (Jardines de Versalles)", 25000, False)
    g.agregar_arista("Cali (Aeropuerto)", "Cantabria (Cueva de Altamira)", 12000, False)


    # MANDA ARGUMENTOS A LA FUNCIÓN GRAFICA

    grafica(G, "Ginebra (CERN)", "California (Silicon)", 8000)
    grafica(G, "Ginebra (CERN)", "Atenas (Acrópolis de Atenas)", 15000)
    grafica(G, "Ginebra (CERN)", "Agra (Taj Mahal)", 20000)
    grafica(G, "Ginebra (CERN)", "Antofagasta (Atacama)", 18000)
    grafica(G, "Ginebra (CERN)", "Cairo (Sahara)", 25000)

    grafica(G, "Cali (Aeropuerto)", "París (Louvre Museum)", 12000)
    grafica(G, "Cali (Aeropuerto)", "Cairo (Sahara)", 18000)
    grafica(G, "Cali (Aeropuerto)", "Hawai (Maui)", 22000)
    grafica(G, "Cali (Aeropuerto)", "Versalles (Jardines de Versalles)", 25000)
    grafica(G, "Cali (Aeropuerto)", "Cantabria (Cueva de Altamira)", 12000)

    grafica(G, "California (Silicon)", "Queensland (Gold Coast)", 12000)
    grafica(G, "California (Silicon)", "Patagonia (Monte Fitz Roy)", 22000)
    grafica(G, "California (Silicon)", "Yucatán (Chichen Itzá)", 18000)
    grafica(G, "California (Silicon)", "Madrid (Museo Nacional del Prado)", 18000)
    grafica(G, "California (Silicon)", "Roma (Roma)", 25000)

    grafica(G, "Atenas (Acrópolis de Atenas)", "Borneo (Borneo Rainforest)", 20000)
    grafica(G, "Atenas (Acrópolis de Atenas)", "Brasilia (Amazonia)", 25000)
    grafica(G, "Atenas (Acrópolis de Atenas)", "Cantabria (Cueva de Altamira)", 18000)
    grafica(G, "Atenas (Acrópolis de Atenas)", "Versalles (Jardines de Versalles)", 22000)
    grafica(G, "Atenas (Acrópolis de Atenas)", "Cancún (Quintana Roo)", 20000)

    grafica(G, "Agra (Taj Mahal)", "Madrid (Museo Nacional del Prado)", 15000)
    grafica(G, "Agra (Taj Mahal)", "París (Louvre Museum)", 12000)
    grafica(G, "Agra (Taj Mahal)", "Gettysburg (Gettysburg National Military Park)", 18000)
    grafica(G, "Agra (Taj Mahal)", "Marrakech (La Palmeraie Marrakech)", 22000)
    grafica(G, "Agra (Taj Mahal)", "Digue (Anse Source d'Argent)", 25000)

    grafica(G, "Antofagasta (Atacama)", "Cairo (Sahara)", 12000)
    grafica(G, "Antofagasta (Atacama)", "Hawai (Maui)", 18000)
    grafica(G, "Antofagasta (Atacama)", "Cuzco (Machu Picchu)", 22000)
    grafica(G, "Antofagasta (Atacama)", "Borneo (Borneo Rainforest)", 15000)
    grafica(G, "Antofagasta (Atacama)", "Bergen (Fiordos de Noruega)", 20000)

    grafica(G, "Cairo (Sahara)", "Queensland (Gold Coast)", 25000)
    grafica(G, "Cairo (Sahara)", "Patagonia (Monte Fitz Roy)", 18000)
    grafica(G, "Cairo (Sahara)", "California (El Capitan)", 22000)
    grafica(G, "Cairo (Sahara)", "Brentwood Bay (Butchart Gardens)", 25000)
    grafica(G, "Cairo (Sahara)", "Marrakech (La Palmeraie Marrakech)", 12000)

    grafica(G, "Hawai (Maui)", "Marathon (Battlefield of Marathon)", 18000)
    grafica(G, "Hawai (Maui)", "Cuzco (Machu Picchu)", 22000)
    grafica(G, "Hawai (Maui)", "Roma (Roma)", 25000)
    grafica(G, "Hawai (Maui)", "Nuevo México (Cuevas de Carlsbad)", 12000)
    grafica(G, "Hawai (Maui)", "Whitsunday Island (Whitehaven Beach)", 18000)

    grafica(G, "Queensland (Gold Coast)", "Paradise Island (Atlantis)", 15000)
    grafica(G, "Queensland (Gold Coast)", "Digue (Anse Source d'Argent)", 20000)
    grafica(G, "Queensland (Gold Coast)", "Thua Hin (Chiva Som)", 22000)
    grafica(G, "Queensland (Gold Coast)", "Alicante (Sha Wellness Clinic)", 25000)
    grafica(G, "Queensland (Gold Coast)", "Costa Azul (Niza)", 12000)

    grafica(G, "Patagonia (Monte Fitz Roy)", "Atacama (Valle de la Luna)", 18000)
    grafica(G, "Patagonia (Monte Fitz Roy)", "Bergen (Fiordos de Noruega)", 22000)
    grafica(G, "Patagonia (Monte Fitz Roy)", "Marrakech (La Palmeraie Marrakech)", 25000)
    grafica(G, "Patagonia (Monte Fitz Roy)", "Paradise Island (Atlantis)", 12000)
    grafica(G, "Patagonia (Monte Fitz Roy)", "Whitsunday Island (Whitehaven Beach)", 18000)

    grafica(G, "California (El Capitan)", "Cantabria (Cueva de Altamira)", 18000)
    grafica(G, "California (El Capitan)", "Nuevo México (Cuevas de Carlsbad)", 22000)
    grafica(G, "California (El Capitan)", "Versalles (Jardines de Versalles)", 25000)
    grafica(G, "California (El Capitan)", "Brentwood Bay (Butchart Gardens)", 12000)
    grafica(G, "California (El Capitan)", "Atacama (Valle de la Luna)", 15000)

    grafica(G, "Yucatán (Chichen Itzá)", "Roma (Roma)", 20000)
    grafica(G, "Yucatán (Chichen Itzá)", "Borneo (Borneo Rainforest)", 25000)
    grafica(G, "Yucatán (Chichen Itzá)", "Brasilia (Amazonia)", 12000)
    grafica(G, "Yucatán (Chichen Itzá)", "Cantabria (Cueva de Altamira)", 18000)
    grafica(G, "Yucatán (Chichen Itzá)", "Nuevo México (Cuevas de Carlsbad)", 22000)

    grafica(G, "Ma'an (Petra)", "Brentwood Bay (Butchart Gardens)", 18000)
    grafica(G, "Ma'an (Petra)", "Atacama (Valle de la Luna)", 22000)
    grafica(G, "Ma'an (Petra)", "Bergen (Fiordos de Noruega)", 25000)
    grafica(G, "Ma'an (Petra)", "Marrakech (La Palmeraie Marrakech)", 12000)
    grafica(G, "Ma'an (Petra)", "Paradise Island (Atlantis)", 15000)

    grafica(G, "Madrid (Museo Nacional del Prado)", "Digue (Anse Source d'Argent)", 20000)
    grafica(G, "Madrid (Museo Nacional del Prado)", "Whitsunday Island (Whitehaven Beach)", 22000)
    grafica(G, "Madrid (Museo Nacional del Prado)", "Thua Hin (Chiva Som)", 25000)
    grafica(G, "Madrid (Museo Nacional del Prado)", "Alicante (Sha Wellness Clinic)", 12000)
    grafica(G, "Madrid (Museo Nacional del Prado)", "Costa Azul (Niza)", 18000)

    grafica(G, "París (Louvre Museum)", "Bergen (Fiordos de Noruega)", 18000)
    grafica(G, "París (Louvre Museum)", "Marrakech (La Palmeraie Marrakech)", 22000)
    grafica(G, "París (Louvre Museum)", "Paradise Island (Atlantis)", 25000)
    grafica(G, "París (Louvre Museum)", "Digue (Anse Source d'Argent)", 12000)
    grafica(G, "París (Louvre Museum)", "Whitsunday Island (Whitehaven Beach)", 15000)

    grafica(G, "Gettysburg (Gettysburg National Military Park)", "Alicante (Sha Wellness Clinic)", 20000)
    grafica(G, "Gettysburg (Gettysburg National Military Park)", "Costa Azul (Niza)", 25000)
    grafica(G, "Gettysburg (Gettysburg National Military Park)", "Cancún (Quintana Roo)", 12000)
    grafica(G, "Gettysburg (Gettysburg National Military Park)", "Grindavik (Blue Lagoon)", 18000)
    grafica(G, "Gettysburg (Gettysburg National Military Park)", "Mendoza (Termas de Cacheuta)", 22000)

    
    #MÉTODO FLOYD WARSHALL
    m_floyd, m_warshall = g.floyd_warshall()
    

    # POR SI DESEAN HACER UN GRAFO NO DIRIGIDO

    #SE IMPRIME EN CONSOLA MATRIZ DE ADYACENCIA
    #g.imprimir_matriz(g.matriz, False)
    #g.imprimir_matriz(m_floyd, False)
    #g.imprimir_matriz(m_warshall, True)



def recorridoLugares():
    print("---------------LUGARES--------------")
    vertices_anchura = g.recorrido_anchura("Cali (Aeropuerto)")
            
    for i in range(len(vertices_anchura)):
        print(f"Ciudad {i+1}: {vertices_anchura[i]}")
            
    input()

def agregarNuevoLugar():

    nombre = input("Ingrese el nombre del nuevo lugar: ")

    g.agregar_vertices(nombre)

    vertices_anchura = g.recorrido_anchura("Cali (Aeropuerto)")

    os.system("cls")
    print("---------------AGREGAR LUGAR--------------")
    for i in range(len(vertices_anchura)):
        print(f"Ciudad {i+1}: {vertices_anchura[i]}")

    print("")

    while True:

        try:
            op = int(input(f"Selecciona la ciudad con la cual desea conectar {nombre}: "))

            if op <= len(vertices_anchura):

                break
            
            else:

                print("Ingresa un número válido")

        except ValueError:

            print("Ingrese un número válido")

    ciudadConectar = ""

    for i in range(op):
        ciudadConectar = vertices_anchura[i]

    os.system("cls")

    while True:

        try:

            distancia = int(input(f"Indique la distancia que hay entre {nombre} y {ciudadConectar}: "))

            break

        except ValueError:

            print("Ingrese un valor válido")
    

    g.agregar_arista(nombre, ciudadConectar, distancia, False)

    grafica(G, nombre, ciudadConectar, distancia)

    os.system("cls")
    print("Lugar asignado correctamente")
    input()


def agregarRelacion():

    ciudadOrigen = ""
    ciudadDestino = ""

    vertices_anchura = g.recorrido_anchura("Cali (Aeropuerto)")
    os.system("cls")

    print("---------------AGREGAR CONEXIÓN--------------")
    for i in range(len(vertices_anchura)):
        print(f"Ciudad {i+1}: {vertices_anchura[i]}")

    print("")
    
    while True:

        print("")

        try:
            op = int(input(f"Selecciona la ciudad de origen: "))

            if op <= len(vertices_anchura):

                break

            else:

                print("Ingrese un número válido")

        except ValueError:
            print("Ingrese un valor correcto")

    for i in range(op):
        ciudadOrigen = vertices_anchura[i]

    os.system("cls")

    aux = 1
    for i in range(len(vertices_anchura)):
        if i != op-1:
            print(f"Ciudad {aux}: {vertices_anchura[i]}")
            aux +=1

    print("")


    while True:

        print("")

        try:
            op2 = int(input(f"Selecciona la ciudad que desea conectar con {ciudadOrigen}: "))

            if op2 <= (len(vertices_anchura)-1):

                break

            else:

                print("Ingrese un número válido")

        except ValueError:
            print("Ingrese un valor correcto")


    os.system("cls")

    aux = 1
    for i in range(len(vertices_anchura)):
        if i != op-1:

            if op2 == aux:
                ciudadDestino = vertices_anchura[i]
            aux +=1

    distancia = int(input(f"Indique la distancia que hay entre {ciudadOrigen} y {ciudadDestino}: "))

    g.agregar_arista(ciudadOrigen, ciudadDestino, distancia, False)
    grafica(G, ciudadOrigen, ciudadDestino, distancia)

    os.system("cls")
    print("Conexión realizada correctamente")
    input()


def graficarGrafo():

    pos = nx.kamada_kawai_layout(G)

    # Dibujar el grafo
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
    plt.show()


def mejorCamino():

    m_floyd, m_warshall = g.floyd_warshall2()

    ciudadOrigen = ""
    ciudadDestino = ""

    vertices_anchura = g.recorrido_anchura("Cali (Aeropuerto)")
    os.system("cls")

    print("---------------CAMINO MÁS CORTO--------------")
    for i in range(len(vertices_anchura)):
        print(f"Ciudad {i+1}: {vertices_anchura[i]}")


    while True:

        print("")

        try:
            op = int(input(f"Selecciona la ciudad de origen: "))

            if op <= len(vertices_anchura):

                break

            else:

                print("Ingrese un número válido")

        except ValueError:
            print("Ingrese un valor correcto")

    for i in range(op):
        ciudadOrigen = vertices_anchura[i]

    os.system("cls")

    aux = 1
    for i in range(len(vertices_anchura)):
        if i != op-1:
            print(f"Ciudad {aux}: {vertices_anchura[i]}")
            aux +=1

    print("")
    
    while True:

        print("")

        try:
            op2 = int(input(f"Selecciona la ciudad de destino: "))

            if op2 <= (len(vertices_anchura)-1):

                break

            else:

                print("Ingrese un número válido")

        except ValueError:
            print("Ingrese un valor correcto")


    os.system("cls")

    aux = 1
    for i in range(len(vertices_anchura)):
        if i != op-1:

            if op2 == aux:
                ciudadDestino = vertices_anchura[i]
            aux +=1

    # Obtener el camino más corto entre los vértices de inicio y fin.
    camino_corto = reconstruir_camino(m_warshall, ciudadOrigen, ciudadDestino)

    print("---------------CAMINO MÁS CORTO--------------")
    print(f"Camino más corto de {ciudadOrigen} a {ciudadDestino}:")

    print(f"1: {ciudadOrigen}")
    for i in range(len(camino_corto)):
        print(f"{i+2}: {camino_corto[i]}")

    print(f"{len(camino_corto)+2}: {ciudadDestino}")
    input()


    caminoCortoGrafica = nx.DiGraph()
        
    try:
        grafica(caminoCortoGrafica, ciudadOrigen, camino_corto[0])
        for i in range(1, len(camino_corto)):
            grafica(caminoCortoGrafica, camino_corto[i-1], camino_corto[i])
            
            if i == len(camino_corto)-1:
                grafica(caminoCortoGrafica, camino_corto[i], ciudadDestino)  
    except IndexError:
        grafica(caminoCortoGrafica, ciudadOrigen, ciudadDestino)
    finally:       
        pos = nx.layout.planar_layout(caminoCortoGrafica)
        nx.draw_networkx(caminoCortoGrafica, pos)
        plt.show()


def menu():

    #MENÚ
    while True:

        os.system("cls")

        #Menú para seleccionar la opción

        print("-----------BIENVENIDO-----------")
        print("1. Visualizar lugares de destino")
        print("2. Agregar nuevo lugar de destino")
        print("3. Agregar relación")
        print("4. Mejor camino entre ciudades")
        print("5. Viusalizar mapa de ciudades")
        print("0. Salir")
        print("")

        try:
        #Guardar
            op = int(input("Seleccione una opción: "))
            os.system("cls")

            if op == 1:

                recorridoLugares()
            
            elif op == 2:

                agregarNuevoLugar()

            elif op == 3:

                agregarRelacion()

            elif op == 4:

                mejorCamino()

            elif op == 5:


                graficarGrafo()

                """
                pos = nx.layout.planar_layout(G)
                nx.draw_networkx(G, pos)
                labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
                plt.show()"""


            
            elif op == 6:

                #graficarCamino()
                print()

            elif op == 0:

                print("ADIÓS")
                input()
                break
            
            else:

                print("Dato ingresado no válido")


        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            input("Presione Enter para continuar.")

menu()


