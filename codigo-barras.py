import os, socket, time
contador = 0
numero = 0

while(contador==0):
    numero = int(input("Lector de etiquetas:"))
    while(numero <= 15):
        print ("Etiqueta Leida: {0}\n".format(numero))
        numero = numero + 1 
        #contador=contador+1
        #comentario de pruebas unitarias
