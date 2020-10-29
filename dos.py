
#!/usr/bin/env python
#-*-coding utf:-8-*-

def main (args):

	x = input ("ingrese una cadena: ")
	m = len (x)
	y =input ("ingrese la subcadena a buscar: ")
	n = len (y)

	bf (x, y, m, n)
	return 0

def bf (x, y, m, n):

	contador = 0
	llave = 0
	for j in range (m -n):

		for i in range (n):

			if (y[i] != x[j+i]):
				contador = 0
				break

			llave = j
			contador = contador +1
			print (contador, llave)

		if (contador == n):
			print ("coincidencia hallada")




if __name__ == '__main__':
	import sys
	sys.exit (main(sys.argv))