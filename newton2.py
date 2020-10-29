import math

p = 1
bandera = 0

for i in range (1, 1000):
    a =  2*math.sin(math.pi * p) - p
    b =  2*math.pi*math.cos(math.pi * p) -1
    p = p -a/b

    if ( a < 0.000000000000000001 and a > 0 ):
        print ("se encontro la raíz en: ", p, "en la iteracion: ", i)
        bandera = 1
        break

        
 


if (bandera == 0):
    print ("no se econtro raíz")