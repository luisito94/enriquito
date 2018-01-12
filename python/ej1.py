#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

#hacer un programa que abra un archivo que cree un hijo, que el padre solicite acceso
#El hijo solicita acceso, el hijo tiene que escribir su pid y el de su padre, y libera, que espera 5 seg
# el padre solicita el acceso espera 1 seg, escriba lo que seay al final se cierra el fichero

import fcntl #import librería de control
import os
import time

filename = '/tmp/pruebaEj1.txt'
fichero = open(filename, 'a')

pid = os.fork() #aquí se desdobla el código

if pid == 0:
	print("Solicitando acceso hiiiijo")
	fcntl.flock(fichero, fcntl.LOCK_EX)
	men = "Soy el hijo y mi pid es: "+str(os.getpid())#+". Soy el hijo y el pid de mi padre es: "+str(os.getppid()
	fichero.write(men)
	time.sleep(5)
	fcntl.flock(fichero, fcntl.LOCK_UN)
	print("Hijo acaba")
	#print("Soy el hijito con un pid: ",os.getpid())
	
else:
	time.sleep(15)
	print("Solicitando acceso padre")
	fcntl.flock(fichero, fcntl.LOCK_EX)
	men2 = "Soy el padre y mi pid es: "+str(os.getpid())
	fichero.write(men2)
	time.sleep(1)
	fcntl.flock(fichero, fcntl.LOCK_UN)
	print("Padre acaba")
	#print("Soy el padre con pid: ",os.getpid())
	#print("Mi hijo tiene pid: ",pid)
print("Acabandoooooouuuu")
fichero.close()