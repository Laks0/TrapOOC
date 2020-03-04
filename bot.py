import random

letras = open("trap.txt", "r")

versos = letras.read().split("\n")

canciones = []

i = 0
c_cancion = [[],""]
while i < len(versos):
	if versos[i] != "-":
		c_cancion[0].append(versos[i])
	else:
		c_cancion[1] = versos[i + 1]
		i += 1
		canciones.append(c_cancion)
		c_cancion = [[],""]

	i += 1

c = canciones[random.randrange(len(canciones))]
n = random.randint(1,3)

v_inicial = random.randint(0,len(c[0]) - n)

txt = ""

for l in range(n):
	txt += c[0][v_inicial + l] + "\n"

txt += "(" + c[1] + ")"

print(txt)