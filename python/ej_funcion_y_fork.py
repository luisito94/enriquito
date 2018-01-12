#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

#pedir que el padre haga un bucle que si pide caracter, cuando se de h, que se ejecute una funcion del hijo
import os
import time

def imprimir_pid():
	print("Mi pid es: ",os.getpid())

def lanza_hijo():
	os.fork()
	pid = os.fork()#aquí se desdobla el código
	if pid == 0:
		imprimir_pid()
		os._exit(0)

while True:
	print("Introduzca una letra por favorrrr")
	nombre = input()
	if nombre == "h":
		lanza_hijo()
	if nombre == "q":
		print("Adiosssss")
		os._exit(0)
#lanza_hijo()
time.sleep(1)
print("Acabando")