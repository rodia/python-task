import random
aciertos = 0
jugar = 1
juegos = 0
total_intentos = 0
total_aciertos = 0
while jugar:
	intento = 0
	aciertos = 0
	lanzamiento = random.randint(1,6)
	while intento < 3:
		apuesta = int(input("Haga su apuesta: "))
		if apuesta > 0 and apuesta <= 6:
			if (apuesta == lanzamiento):
				aciertos += 1
				intento += 1
				print("Acerto!")
				break;
			elif apuesta > lanzamiento:
				print("Muy Alta")
			elif apuesta < lanzamiento:
				print("Muy Baja")
		else:
			print("apuesta invalida")
		intento += 1
	juegos += 1
	total_intentos += intento
	total_aciertos += aciertos
	jugar = int(input("Para intentar nuevamente introduzca 1, para terminar 0: "))

print("Cantidad de juegos", juegos)
print("Cantidad de intentos", total_intentos)
print("Cantidad de aciertos", total_aciertos)
print("porcentaje de aciertos", round((total_aciertos/total_intentos)*100, 2), "%")
