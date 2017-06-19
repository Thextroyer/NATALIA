#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram.ext
from telegram.error import NetworkError, Unauthorized
from time import sleep
import random
import requests
import telegram
import urllib2
import requests
import sys
import os
import time
from hablar import *
from chisal import *
from os.path import basename
from urlparse import urlsplit
from telegram.ext import Updater, CommandHandler



update_id = None

def handle_message(bot, update):


    def habla(frase):
        #HACER QUE COMPRUEBE SI HAY UN AUDIO.WAV YA
        enviar_audio(frase)
        time.sleep(8)
        bot.sendVoice(chat_id=update.message.chat.id, voice=open('audio.wav', 'rb'))
        eliminar_audio()

    query_ans =[
        [ 'hola','como quieres que te llame ?'],
        #[ 'chiste',(str(chisteAl()))],
        [ 'que',"kieres palos?"],
        [ 'llamame',"Vale , te voy a llamar como me salga del capullo"],
        [ 'eres mio',"Yo no soy un objeto no me puedes someter con tus acciones machistas asailfghafu"],
        [ 'es mio',"Yo no soy un objeto no me puedes someter con tus acciones machistas asailfghafu"],
        [ 'feminazi',"Tengo FRASES de mierda para defender ese argumento asdasjdfasfbq ****ERRORR ERRROR 404****** "],
        [ 'cristian',"Pero que dices pallaso , a mi programador lo dejas eh , que te reviento payaso ,"+ update.message.from_user.first_name +" vaya nombre de mierda"],
        [ 'bot eres virgen',"He follao mas que tu pallaso"],
        [ 'me follo a tu madre',"Ya se que te follas a mi placa madre , ya que solo te cabe por un usb pallaso"],
        [ 'te quiero bot',"Y yo a ti "+ update.message.from_user.first_name +",pero nuestro amor es imposible , yo soy un transexual invertido y tu un gay pedernido"],
        [ 'gustas bot',"Ehhh relaja , mariconadas las justas , que Jakier te hackea"],
        [ 'hitler',"HEIL FUHRER"],
        [ 'lenin',"SLAVA LENIN"],
        [ 'dani',"TONTO POLLAS"],
        ]

    id_ands =[[ '278837725',  'Hola cristian , que tal anda jakier'],
            [ '316657468', 'Hola padre , eres un genio'],
            [ 0.,  0.]]

    for i in range(len(query_ans)):
        for j in range(len(query_ans[i])):
            if str(query_ans[i][j]) in update.message.text.lower():
                #habla(str(query_ans[i][j+1]))
                bot.sendMessage(chat_id=update.message.chat.id,text=str(query_ans[i][j+1]))

            else:
                  #AQUÍ VA EL BUCLE FOR QUE RECORRE LOS ARRAYS Y SI NO ES ESO , VA A POR LOS IF , AUNQUE ESTO TENDRÁ QUE CAMBIAR , YA QUE TENDRIA QUE RECORRER OTRO ARRAY PARA CADA
                  #CATEGORÍA , IMAGENES , VIDEOS ETC
                if "arma" in update.message.text.lower():
                    bot.sendMessage(chat_id=update.message.chat.id, text="La has cagado man,hoja de 5mm")
                    bot.sendPhoto(chat_id=update.message.chat.id, photo="https://thumbs.dreamstime.com/t/cuchillo-del-combate-de-la-tenencia-de-la-mano-30923685.jpg")
                    return
                if "gif porno" in update.message.text.lower():
                    listaG = ["http://68.media.tumblr.com/b156e4676b3955e72b70617fffda18aa/tumblr_nw4mjg5SgO1tgc471o1_400.gif","http://i.imgur.com/86VdsV3.gif","http://68.media.tumblr.com/9d43034387b3ec9ad5afa9339678792b/tumblr_n442jcaVPF1rjbi2lo1_400.gif","http://www.pbh2.com/wordpress/wp-content/uploads/2013/10/perfect-butt.gif","http://gif-porno.com/gif553/paseando-con-el-culo-al-aire-por-casa","http://gif-porno.com/gif485/morena-moviendo-el-culo-con-una-polla-dentro","http://3.bp.blogspot.com/-0-ecR5OIjhA/VM-5dCbxpDI/AAAAAAAAAbI/5JXBerfUPOE/s1600/oiled-butt-shaking-porn-animation.gif","http://gif-porno.com/gif428/culo-botando-que-te-hipnotiza","http://38.media.tumblr.com/106b018f0a48997679783889959a269c/tumblr_mwkq1jWrQa1sw8qefo1_500.gif","http://i.imgur.com/jLrZwIs.gif"]
                    bot.sendDocument(chat_id=update.message.chat.id, document=random.choice(listaG))
                    return
                if "foto porno" in update.message.text.lower():
                    archivo = open('imagenes.txt','r')
                    listaF = archivo.readlines()
                    bot.sendPhoto(chat_id=update.message.chat.id, photo= "https://encrypted-tbn0.gstatic.com/" + random.choice(listaF))
                    return
                if "comemela" in update.message.text.lower():
                    bot.sendMessage(chat_id=update.message.chat.id, text="asi?")
                    bot.sendPhoto(chat_id=update.message.chat.id, photo="http://pics.serviporno.com/videos/c/f/d/2/0/cfd20208c4d151cbb98939637dc8fb2f.mp4-preview-11.jpg")
                    return
                if "video sexo" in update.message.text:
                    bot.sendMessage(chat_id=update.message.chat.id, text="https://fck-ce19.tnaflix.com/dev19/0/016/107/0016107887/Nephews_big_cock_fucks_Yasmin_Scotts_pussy_on_top-720p.mp4?speed=195000&secure=_O3D-vDI-aMz9uj4EG0mUQ==,1484283297")
                    return

                if "adri" in update.message.text.lower():
                    if update.message.from_user.id == 278837725 :
                            bot.sendMessage(chat_id=update.message.chat.id, text="TUS ARRAY ME LA CHUPAN")

                    elif update.message.from_user.id == 316657468:
                            bot.sendMessage(chat_id=update.message.chat.id, text="ADRI PUTO AMO")
                    elif update.message.from_user.id == 292736036:
                            bot.sendMessage(chat_id=update.message.chat.id, text="DANI TE VOY A APUÑALAR COMO TE METAS CON ADRI")

                    else:
                            bot.sendMessage(chat_id=update.message.chat.id, text="A VER PAYASO QUE ESTÁS DICIENDO DE MI ADRI?")
                    return
                if "aupa atleti" in update.message.text.lower():
                    bot.sendPhoto(chat_id=update.message.chat.id, photo="http://web.telegram.org/b2caf4d3-574f-4d41-aaa0-162705e65b42")
                    return


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="KE EMPIESE LA FIETA")





def main():
    global update_id
    bot = telegram.Bot('262253767:AAEqMxOBGzwarUxCDwikqvyRr8bpdkF90Is')

    #ESTO HACE QUE EL COMANDO FUNCIONE , TU ARCHIVO LARGO ME LA CHUPA
    updater = Updater(token='262253767:AAEqMxOBGzwarUxCDwikqvyRr8bpdkF90Is')
    dispatcher = updater.dispatcher# <--- esto lo he añadido yo





    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None
    while True:
        try:
            for update in bot.getUpdates(offset=update_id, timeout=10):
                update_id = update.update_id + 1
                if update.message:
                    start_handler = CommandHandler('start', start )
                    dispatcher.add_handler(start_handler)
                    updater.start_polling()


                    print (update)
                    handle_message(bot, update)


        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1


if __name__ == '__main__':
    main()
