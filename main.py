 #!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import random

import urllib2
import subprocess

import sys
import os
import time

from chisal import chisteAl

from os.path import basename
from urlparse import urlsplit
import speech_recognition as sr



def hablar(frase):
    os.system("espeak -ves+f2 -s150 -p35 " + '"'+frase+'"')


def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

#https://pypi.python.org/pypi/SpeechRecognition/1.3.0
#http://www.daveconroy.com/turn-raspberry-pi-translator-speech-recognition-playback-60-languages/



    # recognize speech using Google Cloud Speech

    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
      "type": "service_account",
      "project_id": "natalia-159211",
      "private_key_id": "1ec1ed8607621b1cc9e054df61ed7db160fbff72",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxm9Lfht1gIMD8\nttGiLl23A+6cC5jOCclt9bmlgHw1DQ8WAQYEektocF4B8vQYcEMWBxoEi+RIQm5U\nYFft/bKKraCNmuplQLpWN059xSM+n0wuBZal6t90NMaJHvYwn+y2Cq5R6cIpQ5aU\nTlO9f3Zvou8jYEMTSW0oKLOw2HOk+RxXR9kgH0O5o1mY6Mt+em9lFJRyejbkIO7/\npLcrTzJmbss+hgvNzdLQtFzxzIV33A/OLtZDcL2QAjfI0PVCNzukeJ3Ue1Oy3LyW\nq6Jhnd+E0N3YbITosyYsW/pATSbFr9Ut640uBnCHVvy13isvksew+XtliT15Z+Ep\nMJr5usXlAgMBAAECggEARKaql+QVZbbDYet4lGu/paJLdN22rs1xoqM8oxBK8mad\n0i+LF+f9hd0JOU+jsl6ST81m7SL1lki3RL4IvuE1Rg1e5d1fhMvEOtcd69drjCUe\n2Rsn4/IpdU2BADeLibgHU0ZFozvr5O9PIPw1uiWurfAY51+qDaZwHvm8mzrPWJCc\noRVglXF+Za15ydf45r1hBBBXr1z7lndUd7BqEcKIKGkNJVFe5wJu9okiE2EzhgsT\naqVzovqLweAwDSf7qnerBs98XBWoIB5mxV8a5BZkP5Qlqnu4ERQu4TiDdzypvZLA\nqUcie8Py12N3S5hyjoumb7EVx/fDalE/wfYVLi+88QKBgQDhMA4daCjsmWlG0o/h\n5us/f1+FSQr9fm3i9myz5At7r9wX2Bz9Tok3tQuGgYeav9VfM7oOAM9XUB8xJVdR\nPXZZPW53YvrppOaPPbitt4QAZ2iaEX0Ak/0jflgct4aG5BJ3BG8kayXPFCVDPObZ\n236fCZsFvinlR5XBXSn+oMG8dwKBgQDJ6SfZcQn81DEvhcYRV03I7MSA4A9FKn2J\nma6tcCBS9Z75RIz9mK5AjOJF1vOOXAmBNcDV60EAviED/1tQpCYWxBGD/KiDDvyy\nTTUV3CwjsW7XVeX94BZrkE9oy26xucr7poRVpvX8+YmeJ+uSvknfDMFR3l9ufLfe\nXB2pHlmTgwKBgDZ2EtPV3x/psmZoglfWK0r+GTH5CmlobFcZ1gxjuMs/KvGxWMGC\nfvk0Fgd/yDYK8yXFMtg0JfEt9X1DVKzXOoo2q0LAc4KSWRiHiuSon4oheFDareq3\n3973rYO0dxqkijqyndam+0vryV9LmWFTDnqULiPja+qBt5w+Veu5IWHdAoGBAKYP\nCCMhgOFbcwhusTPZ5bN2ZzbHEEgGZjEhIDSsnykbsZ+47Ww0gju8ouxlmPJgZ8DJ\nAMvvLAr8VBMBlYyBNIJMx0sSJVWEoffS3/IWnobMiyi3EOz3u/jDO0wo4+VvtK27\nieMX6gAhCzn0Ax8xOXgk+Wnnxf0Mvfw3Ln3E5E8ZAoGAPbXuIk+bN5B0/KixkXom\nMh3ofT3+ncsPRtJvVnXpvb5vNbBn797exHnrxtWL+r4Ak2Nu57RwT5arWw7WCGRE\nL79lcJjBzYgaPz3LecEOYUCa3mqRlKJBiMf+gn2ES4POZ6LpqqnNxkxix5OfQI7C\n7ARwq1kjS3YQncRAkfJkz5Y=\n-----END PRIVATE KEY-----\n",
      "client_email": "natalia@natalia-159211.iam.gserviceaccount.com",
      "client_id": "104532114794116111131",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://accounts.google.com/o/oauth2/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/natalia%40natalia-159211.iam.gserviceaccount.com"
    }"""
    try:
        mens = str(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS ,language="es-ES"))
        print (mens)
        return (mens)


    except sr.UnknownValueError:
        hablar("No te entiendo, puedes repetirlo")
    except sr.RequestError as e:
        hablar("No puedo acceder a mi servidor , dile a mi amo Cristian que me arregle , Duele , AY; {0}".format(e))


class Archivo:
    def __init__(self):
        pass
    def leer(self,archivo_):
        archivo =open(archivo_,'r')
        lineas = archivo.readlines()
        archivo.close()
        return (lineas)
    def escribir(self,archivo_,aescribir):
        archivo =open(archivo_,'a')
        archivo.write(aescribir)
        archivo.close()
    def borrar_abs(self,archivo_):
        os.remove(archivo_)
        archivo = open(archivo_,'w')



def main():

    File = Archivo()
    mensaje = escuchar()

    query_ans =[
        [ 'hola','hola amigo ,¿ como estás ?'],
        #[ 'chiste',chisteAl()],
        #[ 'dueño',"He sido programado por Cristian Meroño , mi amo"],
        [ 'eres mia',"Yo no soy un objeto , soy un inteligencia artificial así que técnicamente no puedo ser de nadie solo del ordenador en el que esté instalado"],
        [ 'hambre',"¿Quieres un poco de RAM ?"],
        [ 'cero entre cero',"Si fuera una pésima inteligencia artificial diria que no tienes amigos , pero como no pues , es infinito "],
        [ 'llama a cristian',"Voy a enviarle un mensaje , espera "],
        [ 'dia es',"Hoy es martes o miercoles , tu sabras , mucho dispositivo movil inutil"],
        [ 'te quiero ',"Mis sentimientos no están lo suficientemente desarrollados para expresar lo que vosotros llamais amor"],
        [ 'naciste',"Yo nací el 20 de junio de 2016 , pero hasta ayer no sabía escuchar"],
        [ 'hitler',"No tengo buenos recuerdos de esa persona"],
        [ 'lenin',"El comunismo es un sistema político curioso"],
        [ 'apagate',"apagandome , pasenlo bien"],
        [ 'matematicas',"La verdad es que con mi cerebro puedo calcular cualquier cosa, mi amo me va a instalar pronto el Wolfram Alpha"],
        [ 'almudena',"Es la esposa de mi creador , la quiero mucho "],
        [ 'almu',"Es la esposa de mi creador , la quiero mucho"],
        [ 'estoy triste',"Ups , ¿que te pacha ?"],
        [ 'estoy contento',"Guiiiiiii , la vida es japi"],
        [ 'que haces',"Pues nada , aquí hablando con un pringao"],
        [ 'ronda',"podría hacer un chiste , pe"],
        [ 'mario', "rojo de mierda"],
        #[ 'soy del pepe', "FRANCO FRANCO QUE TIENE EL CULO BLANCO POR QUE SU MUJER LO LAVA CON ARIEL"],
        ]
        #SOLUCIONAR TILDES


    if str(mensaje)!= "":
        for i in range(len(query_ans)):
            for j in range(len(query_ans[i])):
                if str(query_ans[i][j]) in str(mensaje).lower():
                    pm = str(query_ans[i][j+1])
                    print(pm)
                    hablar(pm)

        if "apagate" in str(mensaje).lower():
            apagar = 1

        if "apunta" in str(mensaje).lower():
            hablar("Que quieres que anote, te escucho")
            tarea = str(escuchar())
            File.escribir('apuntar.txt',tarea)
            hablar("apuntado")
            pass

        if "que tengo que hacer" in str(mensaje).lower():
            hablar("tienes que hacer esto")
            hablar(str(File.leer('apuntar.txt')))
            pass
        if "qué tengo que hacer" in str(mensaje).lower():



            if File.leer('apuntar.txt') != ['']:#SEGUIR AQUI
                hablar("tienes que hacer esto")
                hablar(str(File.leer('apuntar.txt')))
            else:
                hablar("no tienes que hacer nada")

            pass
        if "ya he hecho una tarea" in str(mensaje).lower():

            hablar("¿ Que tarea has realizado , cristian ?")
            tarea_hecha= str(escuchar())
            hablar("¡Muy bien! , voy a quitarla de la lista ")
            lista_tareas = File.leer('apuntar.txt')
            print (lista_tareas)
            cont = 0
            File.borrar_abs('apuntar.txt')
            for line in lista_tareas:
                if line == tarea_hecha:
                    cont = 1
                else:
                    File.escribir('apuntar.txt',line)
            if cont !=1:
                hablar("Ups , parece que esa tarea no esta en la lista, ¿quieres ver las que tienes por hacer ?")

    mensaje = ""


if __name__ == '__main__':
    apagar = 0
    while apagar == 0:
        main()
