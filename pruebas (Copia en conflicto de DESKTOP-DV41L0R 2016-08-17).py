#encoding: utf-8

import serial
import chisal
import alarma
import os
import puerta
import aviso

def Hablar(texto):

	os.system('espeak -v mb-es2 -s 120 -p 93 "' +texto+'"')


class Natalia:

    def __init__(self):
        pass


    def Lampara(self,lampara):

        if lampara == 1:
            #encender relé que pertenece a Lampara
            Hablar("Lampara encendiendose")



        else:
            Hablar("Lampara apagandose")




    def Ventilador(self,ventilador):
        if ventilador == 1:
            #activar relé que pertenece a ventilador
            Hablar("ventilador encendiendose")
        else:
            #apagar relé que pertenece a ventilador
            Hablar("ventilador apagandose")

    def Alarma(self,horas,text):

        #Aqui tendrá que ejecutar el script alarma.py en otra terminal
        segs = horas*3600

        alarma.Alarma(segs,text)

    def Mensaje(self,destinatario,msg):
        #YowSup enviará un mensaje al destinatario que hayamos seleccionado
        Hablar("Mensaje enviado a " + destinatario)

    def Saludar(self,persona):
        if persona == "Lucia" or "Lucía":
            Hablar ("Hola caballo")

        elif persona == "Noe" or "Noelia":

            Hablar("Hola Natalia Apoculo Suicida Wiwi Absurdidez ejem que diga Hola hermana como estás")

        elif persona == "Almu" or "Almudena":

            Hablar("Hola bollo")

        elif persona =="Carmen" or " Carmen Maria" or "Carmen María":
            Hablar("Hola madre de el señor Cristan")
        elif persona == "Pascual":
            Hablar("Hola Pascual , dejate los videos")
        else:
            Hablar("No te conozco , dile a mi amo Cristian que programe un mensaje para ti")





    def Identificar(self,orden):

        cadena = orden[17:len(orden)]
        accion = False
        if orden.startswith("Natalia") or orden.startswith("natalia") == True:
            #orden="Natalia enciende la luz"
            if orden.endswith("lampara") == True:
                accion = True
                if orden.find("enciende",8,17) != -1:
                    natalia.Lampara(1)
                else :
                    natalia.Lampara(0)
            if orden.endswith("puerta")==True:
                accion = True
                if orden.find("abre",8,13) != -1:
                    natalia.Puerta(1)
                else:
                    natalia.Puerta(0)

            if orden.endswith("ventilador") == True:
                accion = True
                if orden.find("enciende",9,17)!=-1:
                    natalia.Ventilador(1)
                else:
                    natalia.Ventilador(0)
            #Natalia saluda a Lucia
            if orden.find("saluda",8,17)!= -1:
                accion = True
                natalia.Saludar(cadena)

            if orden.endswith("chiste"):
                accion = True
                Hablar(chisal.chisteAl())

            if accion ==False:
                Hablar("No se hacer eso mi amo")
        else:
            Hablar ("Hola soy Natalia , que quieres que haga ?")

natalia = Natalia()
entrada = input(Hablar("Que desea mi amo ?"))
natalia.Identificar(entrada)
