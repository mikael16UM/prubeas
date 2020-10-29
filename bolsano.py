#!/usr/bin/env python
#-*-coding utf: -8-*-

import math

def main (args):

	
	print ("de que grado es la expresion")
	grado = int (input ())

	coeficiente = []
	conteo = 0

	while (conteo <=grado):
		xsx = grado-conteo
		print ("ingrese el coeficiente de x^", xsx)
		coeficiente.append(float(input()))  
		conteo = conteo +1

	
	print ("en que intervalo lo recibe")
	a = float(input ())
	b = float (input ())

	#hallar el valor medio del intervalo

	p1 = a + (b -a)/2

	bandera = 0

	while (bandera == 0):
		bandera =Escero (p1, coeficiente, grado)

		if (bandera == 1):
			print (p1, " es el P tal que f(p) = 0")

		else :
			a1 =fdex (a, coeficiente, grado)
			b1 = fdex (b, coeficiente, grado)
			p2 = fdex (p1, coeficiente, grado)

			if (signo (a1) == signo (p2)):
				a = p1
				p1 =  a + (b -a)/2
			else:
				b = p1
				p1 =  a + (b -a)/2		

	return 0


def signo (valor):
	if (valor < 0):
		return -1
	else:
		return 1


def fdex (p1, coeficiente, grado):
	temp = grado
	suma = 0
	j = 0
	while (temp >= 0 and j <= grado):

		suma = suma + coeficiente[j] * pow(p1, temp)
		j = j+1
		temp = temp -1

	return suma	

def  Escero (p1, coeficiente, grado):

	if (fdex (p1, coeficiente, grado )== 0):
		#print (p1, fdex (p1, coeficiente, grado))
		return 1
	return 0



if __name__ == '__main__':
	import sys
	sys.exit (main (sys.argv))