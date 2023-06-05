# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import shutil
from time import sleep

def mainLoop(path, pathfinal, separador):
    #Extraemos la lista de Ficheros y Directorios del path Destino.
    listasNombres = nombreFicherosDestino(pathfinal, separador)
    listaDir = listasNombres[0]
    listaFicheros= listasNombres[1]

    #Creamos unas listas para saber qué Ficheros y Directorios se han añadido al path Destino.
    listaAñadidos=[]
    listaFicherosAñadidos=[]
    listaDirectoriosAñadidos = []

    #Recorremos el Directorio Origen.
    for nombre_directorio, dirs, ficheros in os.walk(path):
        #Separamos el Directorio hijo del Directorio Origen.
        ndirsplit=nombre_directorio.split(separador, maxsplit=2)[1]
        if ndirsplit not in listaDir:
            #Juntamos el Directorio que no está en Destino con el path general de Destino.
            directorioDestino = pathfinal+ndirsplit
            print('Se va a copiar el siguiente Directorio: ' + directorioDestino)
            #Copiamos el Directorio entero en el path Destino.
            shutil.copytree(nombre_directorio, directorioDestino)
            #Sacamos la información de todos las Carpetas hijas del directorio que hemos añadido.
            listaDirAñadidos = nombreFicherosDestino(directorioDestino, separador)[0]
            #Añadimos estas carpetas en la listaDirectoriosAñadidos para tener un control de lo que se ha copiado.
            listaDirectoriosAñadidos.extend(listaDirAñadidos)
            #Se añaden las carpetas en la lista de Directorios Destino
            listaDir.extend(listaDirAñadidos)
            print('Se ha finalizado la copia del Directorio')

        #Recorremos cada uno de los ficheros
        for nombre_fichero in ficheros:
            #Comprobamos is se encuentran en la lista de ficheros destino que hemos extraido
                if nombre_fichero not in listaFicheros:
                    print('Se va a copiar el siguiente Fichero: ' + nombre_fichero)
                    #Se copia el Fichero en el directorio Destino
                    ficheroDestino = pathfinal + ndirsplit +"/"+ nombre_fichero
                    ficheroOrigen = nombre_directorio +"/"+ nombre_fichero
                    print(ficheroOrigen, ficheroDestino)
                    shutil.copy(ficheroOrigen, ficheroDestino)
                    #Se añaden los Ficheros en la listaFicherosAñadidos para tener un control de lo que se ha copiado.
                    listaFicherosAñadidos.append(nombre_fichero)
                    print('Se ha finalizado la copia del Fichero')

    listaAñadidos.append(listaFicherosAñadidos)
    listaAñadidos.append(listaDirectoriosAñadidos)
    return listaAñadidos
# Extraer lista de los nombres de los ficheros del Directorio donde se van a copiar las Fotos.
def nombreFicherosDestino(path,separador):
    listFiles = []
    listDir = []
    listsNames = []
    for dirpath, dirname, filename in os.walk(path):
        listFiles.extend(filename)
        if os.path.isdir(dirpath):
            listDir.append(dirpath.split(separador, maxsplit=2)[1])

    listsNames.append(listDir)
    listsNames.append(listFiles)

    return listsNames


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while(True):
        print('*********Iniciando proceso de COPIADO de Imagenes*********')
        pathOrigen = "F:/AllFotosOfMyLive"
        pathDestino = "C:/Users/lucas/Pictures/AllFotosOfMyLive"
        separador = "AllFotosOfMyLive"
        listAñadidos = []
        print('Ruta Origen: ' + pathOrigen)
        print('Ruta Destino: ' + pathDestino)
        listAñadidos = mainLoop(pathOrigen, pathDestino, separador)
        print('*********Se ha finalizado el proceso de COPIADO de Imagenes*********')
        print('Se han copiado los siguientes Directorios')
        print(listAñadidos[1])
        print('Se han copiado los siguientes Ficheros')
        print(listAñadidos[0])
        sleep(5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
