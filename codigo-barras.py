import os, socket
contador = 0
numero = 0

while(contador==0):
    numero = int(input("Leyendo Etiquetas:"))
    while(numero != 0):
        print ("Etiqueta Leida: {0}\n".format(numero))
        numero = 0
        #contador=contador+1
