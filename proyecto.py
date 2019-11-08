from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os, socket,time

contador = 0;
post_fields = {'ID': 2,'nparte': 12345678910} 
url = 'http://bi.agelectronica.com/botonera/scanner.php' # URL Destino
REMOTE_SERVER = "www.google.com"

lista = []

def conexion():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        IpAd = socket.gethostbyname(host)
        print("Conectado a Internet, IP: {0}".format(IpAd))
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        print("No hay internet favor de conectar la Tarjeta...")
        time.sleep(5)
        return False

def menu():
    
    #os.system("cls") # NOTA para windows cls / Linux clear
    print ("Selecciona una opcion")
    print ("\t\n 1 - Leer Etiqueta")
    print ("\t\n 2 - Mostrar Etiquetas")
    print ("\t\n 3 - Salir")
    
while True:
    while conexion():
        menu()

        opcionMenu = input("Teclea la opcion>> ")


        if opcionMenu=="1":
            print ("")
            numero = int(input("Leyendo Etiquetas:"))
            if(numero):
                lista.append(numero)
                post_fields['nparte'] = numero
                request = Request(url, urlencode(post_fields).encode())
                json = urlopen(request).read().decode()
                #print(json)
                print ("Etiqueta Leida: {0}\n".format(numero))

        elif opcionMenu=="2":
            print ("Opcion 2")
            for ID,VAL in enumerate(lista):
                print("ID Etiqueta: {0} - Valor: {1}".format(ID+1,VAL))
            input("\nPulsa ENTER para continuar")

        elif opcionMenu=="3":
            break

        else:
            input("Opcion Incorrecta")
    break