#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

#ficheros en python
#incluir librería con import
import os


filename = "/tmp/prueba.txt"

#para abrir un fichero hay que abrir una especie de descriptor de fichero
#el segundo parámetro es el modo en el que se abre el fichero
fichero = open(filename, 'w')

#para poder ejecutar con ./ hay que dar permisos al archivo(chmod a+x nombrefichero.py)
fichero.write("Hola mundo. Fichero")
fichero.close()

#para leer
fichero = open(filename, 'r')
leido = fichero.read()
print("lo que hay en el fichero es: ",leido)

#abrir el fichero en modo lectura y escritura
#Lo que pasa es que hay un cursor que al escribir, por ejemplo una letra, se posiciona en el primer carácter y lo sobreescribe
#pero si quisieras leer el archivo en modo 'r+', sacarías por pantalla a partir de donde está posicionado el cursor, en este caso
#a partir de la posición 1, por tanto el primer carácter nuevo que escribieramos, no lo leería.
#los ficheros se pueden abrir en, w+(machaca todo el fichero), r+(sobreescribe, pero mantiene el resto del fichero, si no es mas grande) y
#a+(posiciona el cursor al final y escribe en el fcihero).
fichero = open(filename, 'r+')
fichero.write("g")
leido = fichero.read()
print("Lo nuevo leído: ",leido)

