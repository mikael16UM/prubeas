#creacion de la clase
class conexion :
	def __init__ (self, origin, destiny, cost):
		self.origin = origin
		self.destiny = destiny
		self.cost = cost
		
	def show (self):
		print (self.origin, self.destiny, self.cost)

#crea el objeto y lo mete en el arreglo
def concatenar ( origen, destino, costo, arreglo):
    x = conexion (origen,destino, costo)
    arreglo.append(x)

#bool para saber si es un or
def esOperador (letra):
    if (letra == '|'):
        return 1
    return 0
    
def main ():

    a = input ("ingrese una oracion: ") 
    list (a)
    j = 0 #indice de origen
    h = j +1 #indice de destino
    arreglo = []
    
    #recorre la expresion y crea las conexiones
    for i in a :

        if (esOperador(i) == 1):
            concatenar(j, h, 'E', arreglo)
            j = h
            h = h+1
        else:
            concatenar (j, h, i, arreglo)
            j = h
            h = h+1


    #muestra las conexiones
    for i in arreglo :
        i.show()
    return 0


main()