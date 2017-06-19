import os
import time
import script


def Alarma(segundos,texto):

	#calcular de cuantos segundos hay que hacer la pausa hasta que hable y diga "Tal"


	time.sleep(segundos)
	os.system('espeak -v mb-es2 -s 120 -p 93 "' +texto+'"')


	 Hablar("Alarma programada para dentro de "+ segundos/3600 + "horas")
