#!/usr/bin/python3
#-*-encoding: UTF-8 -*-

import pickle

filename = '/tmp/ficherosBinary.txt'
fichero = open(filename, 'wb')

variable = 'texto'

pickle.dump(variable, fichero)
fichero.close()

fichero = open(filename, 'rb')
leido = pickle.load(fichero)

print(leido)