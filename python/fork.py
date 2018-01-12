#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

#incluir librería con import
import os

pid = os.fork() #aquí se desdobla el código

if pid == 0:
	print("Soy el hijito con un pid: ",os.getpid())
	os._exit(0)
else:
	print("Soy el padre con pid: ",os.getpid())
	print("Mi hijo tiene pid: ",pid)
print("Acabandoooooouuuu")