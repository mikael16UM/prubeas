#!/usr/bin/env python
#-*-coding utf: -8-*-

def main (args):

	x = input ("ingrese texto: ")
	y = input ("ingrese cadena a buscar: ")
	m = len (x)
	n = len (y)
	
	MP (y, n, x, m)

	return 0;
		#recibe la subcadena, su tamaño y un array de enteros

def preMP (x, m, mpNext):
	
	j = -1
	mpNext[0] = -1
	i = 0
	
	while (i < m):

		while (j > -1 and  x[i]!= x[j]):

			j = mpNext [j]

		i = i+1
		j = j+1
		mpNext [i] = j

	#print (mpNext)


def MP (x, m, y, n ):

	mpNext = [0] * (n +1)
	bandera = 0

	preMP (x, m, mpNext)

	i = j = 0

	while ( j < n):

		while ( i > -1 and x[i] != y[j]):

			i = mpNext[i]

		i = i+1
		j = j +1

		if (i >= m):

			print (j-i)
			print ("cadena hallada")
			i = mpNext [i]
			bandera = 1

	if (bandera == 0):
		print ("no se encontraron coincidencias")





if __name__ == '__main__':
	import sys
	sys.exit (main (sys.argv))