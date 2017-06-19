import tweepy
import time
#AUTENTICACIÓN

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

api.send_direct_message(screen_name= "TechAsATeen",
text = "Alguien ha accedido a tu batcueva sin tu permiso" + time.strftime("%d/%m/%y") + "a las " +time.strftime("%H:%M:%S") )
