import os
import serial
import time
import tweepy
import script

ser = serial.Serial('/dev/ttyACM0', 9600) #inicializamos el puerto de serie a 9600 baud

consumer_key = "Juy51lHw6wTnmAeSluFe8U3Fb"
consumer_secret = "	dLwVr6rWk8x5wurnj0PEgSnRP69TqEPUDvI2oQZmqL4UQ9Nbmq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Ahora necesitamos el access token para los permmisos
redirect_url = auth.get_authorization_url()
verifier = "301550918-Ram6SeTMEKDD9NvaZto69vECc68S3FsqUedmRqbu"

# Obtenemos y pasamos al objeto 'auth' el token con el codigo antes provisto
auth.get_access_token(verifier)

# Obtenemos un objeto api que necesitaremos para hacer los requests a Twitter
api = tweepy.API(auth)   # Pasando el objeto 'auth' como parámetro

fecha = time.strftime("%d/%m/%y")
hora = time.strftime("%H:%M:%S")

#TIENE QUE ESPERAR A QUE ALGUIEN HABRA LA PUERTA
#ESTARÁ EN BUCLE ESPERANDO A LA ENTRADA DEL MÓDULO RFID

class Puerta:
    def __init__(self):
        pass

    def creartxt():

        archi=open(fecha+" - " + hora,'w')
        archi.close()

    def aviso():
        api.send_direct_message(screen_name= "TechAsATeen",
        text = "Alguien ha accedido a tu batcueva sin tu permiso" + "el dia" +fecha) + "a las " + hora )





bucle = 3
datos = "0"
detector = 0
estado_accion_puerta = 0
Puerta = Puerta()

while bucle == 3:
    #aqui deberia leer datos de Arduino
    datos = str(ser.readline())
    #aquí habría que desenredar los números que pasa
    if datos != "0":
        detector = int(datos[0])
        estado_accion_puerta = int(datos[1])


    if estado_accion_puerta == 2:
        Hablar("Espero verle pronto señor Cristian")


    else if estado_accion_puerta == 1:

        Puerta.creartxt()
        Hablar("Hola señor Cristian , me alegro de que esté de vuelta")

        Hablar("Si desea algo tan solo tiene que decírmelo")

        #AQUI SE EJECUTARIA EL ROLLO DE SIEMPRE PREGUNTANDO SI QUIERO ALGO
        #guardar registro en el blog de notas
        #si está abierta
        time.sleep(2.0)
    else if detector == True:
        #avisar por tw
        Puerta.aviso()
