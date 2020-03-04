import random

canciones = ["Tumbado el Club",
"Goteo",
"c90",
"Casipegao",
"Para Sacarmelo",
"Kaiosama",
"Like Boss",
"So Fresh",
"Ni Bien Ni Mal",
"Cartoon Network",
"La Cancion",
"McFly",
"High"
]

c_titulo = canciones[len(canciones) - 1]#[random.randrange(len(canciones))]

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

txt += "(" + artista + ")"

print(txt)