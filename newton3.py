import math

p= 0.8
bandera =0
for i in range (1, 1000):
    a =  3*pow(p,2)- math.exp(p)
    b =  6*p - math.exp(p)
    p = p -a/b

    if ( a < 0.00000000001 and a > 0 ):
        print ("se encontro la raíz en: ", p, "en la iteracion: ", i)
        bandera = 1
        break

        
 


if (bandera == 0):
    print ("no se econtro raíz")
