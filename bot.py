import tweepy
from secrets import *

import random

from canciones import *

c_titulo = canciones[random.randrange(len(canciones))]

c_arhivo = open(c_titulo + ".txt", "r")

versos = c_arhivo.read().split("\n")

letra = []
artista = ""

for i, v in enumerate(versos):
	if i < len(versos) - 1:
		letra.append(v)
	else:
		artista = v

n = random.randint(1,3)
verso_inicial = random.randint(0, len(letra) - n)

txt = ""

for i in range(n):
	txt += letra[verso_inicial + i] + "\n"

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

api.update_status(txt.encode("latin1").decode("utf-8"))
#print(txt)

tweet = api.user_timeline(id = api.me().id, count = 1)[0]
api.update_status("(" + artista + ")", tweet.id)